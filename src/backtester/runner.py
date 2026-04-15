import sys
import importlib.util
from backtester import run_backtest


def load_module(filepath):
    spec = importlib.util.spec_from_file_location("strategy_module", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python runner.py <dataset.csv> <strategy.py>")
        sys.exit(1)

    dataset_path  = sys.argv[1]
    strategy_path = sys.argv[2]

    print("Dataset :", dataset_path)
    print("Strategy:", strategy_path)

    module = load_module(strategy_path)

    results = run_backtest(module, dataset_path, verbose="--verbose" in sys.argv)

    print("\n" + "=" * 60)
    print("  BACKTEST RESULTS")
    print("=" * 60)
    print(f"  Composite Return : {results['total_return']:.4f}%")
    print(f"  Avg Sharpe Ratio : {results['sharpe_ratio']:.4f}")
    print(f"  Total Trades     : {results['total_trades']}")
    print(f"  Net P&L          : ${results['final_value']:.2f}")
    print("-" * 60)
    print(f"  {'Dataset':<25} {'Return%':>8}  {'Sharpe':>8}  {'Trades':>7}  {'Net P&L':>10}")
    print(f"  {'-'*25} {'-'*8}  {'-'*8}  {'-'*7}  {'-'*10}")
    for name, r in results["per_dataset"].items():
        print(f"  {name:<25} {r['total_return']:>8.4f}  {r['sharpe_ratio']:>8.4f}  {r['total_trades']:>7}  ${r['final_value']:>9.2f}")
    print("=" * 60)