import pandas as pd
import numpy as np

STARTING_CASH = 10_000.0
"""
DATASETS = [
    {"name": "Heisenberg_crystals", "func": "strategy_dataset1", "prefix": "dataset1", "weight": 1.0},
    {"name": "Pieces_of_eight", "func": "strategy_dataset2", "prefix": "dataset2", "weight": 1.0},
    {"name": "Compound_V_vials", "func": "strategy_dataset3", "prefix": "dataset3", "weight": 1.0},
    {"name": "Solaris_Stardust", "func": "strategy_dataset4", "prefix": "dataset4", "weight": 1.0},
    {"name": "Valyrian_steel" , "func": "strategy_dataset5", "prefix": "dataset5", "weight": 1.0},
    {"name": "Infinity_Stones", "func": "strategy_dataset6", "prefix": "dataset6", "weight": 1.0},
]
"""
# DATASETS = [
#     {"name": "Heisenberg_crystals", "func": "strategy_Heisenberg_crystals","prefix":"Heisenberg_crystals", "weight": 1.0},
#     {"name": "Pieces_of_eight", "func": "strategy_Pieces_of_eight", "prefix": "Pieces_of_eight", "weight": 1.0},
#     {"name": "Compound_V_vials", "func": "strategy_Compound_V_vials", "prefix": "Compound_V_vials", "weight": 1.0},
#     {"name": "Solaris_Stardust", "func": "strategy_Solaris_Stardust", "prefix": "Solaris_Stardust", "weight": 1.0},
#     {"name": "Valyrian_steel" , "func": "strategy_Valyrian_steel", "prefix": "Valyrian_steel", "weight": 1.0},
#     {"name": "Infinity_Stones", "func": "strategy_Infinity_Stones", "prefix": "Infinity_Stones", "weight": 1.0},
# ]

DATASETS = [
    {"name": "Heisenberg_Crystals", "func": "strategy_Heisenberg_Crystals", "prefix": "Heisenberg_Crystals",  "weight": 0.2},
    {"name": "Pieces_Of_Eight",     "func": "strategy_Pieces_Of_Eight",     "prefix": "Pieces_Of_Eight",     "weight": 0.008}, 
    {"name": "Compound_V_Vials",    "func": "strategy_Compound_V_Vials",    "prefix": "Compound_V_Vials",     "weight": 0.25},
    {"name": "Solaris_Stardust",    "func": "strategy_Solaris_Stardust",    "prefix": "Solaris_Stardust",     "weight": 0.5},
    {"name": "Valyrian_Steel",      "func": "strategy_Valyrian_Steel",      "prefix": "Valyrian_Steel",       "weight": 0.5},
    {"name": "Infinity_Stones",     "func": "strategy_Infinity_Stones",     "prefix": "Infinity_Stones",      "weight": 0.0001},
]


MAESTRO_COLS = ["Ace", "King", "Queen", "Jack", "Black_Joker", "Red_Joker"]


def _backtest_single(strategy_func, df, prefix, verbose=False):
    cash     = STARTING_CASH
    shares   = 0.0
    position = "FLAT"
    prev_value   = STARTING_CASH
    daily_pnl    = []
    trade_count  = 0

    if verbose:
        print(f"\n{'TIMESTAMP':<12} {'SIGNAL':<8} {'POS':<6} {'DAILY_PNL':>12} {'TOTAL_VALUE':>12}")
        print("-" * 54)

    for _, row in df.iterrows():
        bar = {
            "timestamp":   str(row["timestamp"])[:10],
            "open":   float(row[f"{prefix}_open"]),
            "high":   float(row[f"{prefix}_high"]),
            "low":    float(row[f"{prefix}_low"]),
            "close":  float(row[f"{prefix}_close"]),
            "volume": float(row.get(f"{prefix}_volume", 0)),
        }
        for col in MAESTRO_COLS:
            bar[col] = float(row.get(col, 0))

        signal = strategy_func(bar)
        price  = bar["close"]

        if signal == "LONG":
            if position == "FLAT":
                qty = cash // price
                if qty > 0:
                    shares = qty; cash -= qty * price; position = "LONG"; trade_count += 1
            elif position == "SHORT":
                cash -= shares * price; shares = 0
                qty = cash // price
                if qty > 0:
                    shares = qty; cash -= qty * price; position = "LONG"; trade_count += 1

        elif signal == "SHORT":
            if position == "FLAT":
                qty = cash // price
                if qty > 0:
                    shares = qty; cash += qty * price; position = "SHORT"; trade_count += 1
            elif position == "LONG":
                cash += shares * price; shares = 0
                qty = cash // price
                if qty > 0:
                    shares = qty; cash += qty * price; position = "SHORT"; trade_count += 1

        elif signal == "FLAT":
            if position == "LONG":
                cash += shares * price; shares = 0; position = "FLAT"; trade_count += 1
            elif position == "SHORT":
                cash -= shares * price; shares = 0; position = "FLAT"; trade_count += 1

        if position == "LONG":   value = cash + shares * price
        elif position == "SHORT": value = cash - shares * price
        else:                     value = cash

        pnl = value - prev_value
        daily_pnl.append(pnl)
        prev_value = value

        if verbose:
            print(f"{bar['timestamp']:<12} {signal:<8} {position:<6} {pnl:>12.2f} {value:>12.2f}")

    if position != "FLAT":
        last_price = float(df.iloc[-1][f"{prefix}_close"])
        if position == "LONG": cash += shares * last_price
        else:                  cash -= shares * last_price
        prev_value = cash

    final_value  = prev_value
    total_return = (final_value - STARTING_CASH) / STARTING_CASH * 100
    returns_arr  = np.array(daily_pnl) / STARTING_CASH
    sharpe = 0.0
    if len(returns_arr) > 1 and returns_arr.std() > 0:
        sharpe = float((returns_arr.mean() / returns_arr.std()) * np.sqrt(252))

    return {
        "total_return":  round(total_return, 4),
        "sharpe_ratio":  round(sharpe, 4),
        "total_trades":  trade_count,
        "final_value":   round(final_value, 2)-10000,
    }


def run_backtest(module, dataset_path, verbose=False):
    df = pd.read_csv(dataset_path)
    df = df.sort_values("timestamp").reset_index(drop=True)

    per_dataset         = {}
    weighted_return_sum = 0.0
    weight_total        = 0.0
    total_trades        = 0

    for ds in DATASETS:
        func_name = ds["func"]
        if not hasattr(module, func_name):
            raise ValueError(
                f"Strategy file is missing function: {func_name}(bar)\n"
                f"All 6 required: " + ", ".join(d["func"] for d in DATASETS)
            )
        strategy_func = getattr(module, func_name)

        if verbose:
            print(f"\n{'='*54}\n  {ds['name']}\n{'='*54}")

        result = _backtest_single(strategy_func, df, ds["prefix"], verbose=verbose)
        per_dataset[ds["name"]]  = result
        weighted_return_sum     += result["total_return"] * ds["weight"]
        weight_total            += ds["weight"]
        total_trades            += result["total_trades"]
        
        # print(result["total_return"]*ds["weight"]*100)
        # print(ds["weight"])
        if verbose:
            print(f"\n  Return: {result['total_return']}%  Sharpe: {result['sharpe_ratio']}  Trades: {result['total_trades']}")

    composite_return = weighted_return_sum 
    avg_sharpe       = sum(d["sharpe_ratio"] for d in per_dataset.values()) / len(per_dataset)
    final        = (composite_return*STARTING_CASH)/100
    # print(final)
    if verbose:
        print(f"\nCOMPOSITE RETURN: {composite_return:.4f}%  AVG SHARPE: {avg_sharpe:.4f}  TOTAL TRADES: {total_trades}\n")

    # print(composite_return)
    return {
        "total_return":  round(composite_return, 4),
        "sharpe_ratio":  round(avg_sharpe, 4),
        "total_trades":  total_trades,
        "final_value":   round(final, 2),
        "per_dataset":   per_dataset,
        
    }
