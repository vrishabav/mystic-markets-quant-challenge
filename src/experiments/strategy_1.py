import math

# Global state to keep track of historical prices per asset
history = {
    "Heisenberg_Crystals": [],
    "Pieces_Of_Eight": [],
    "Compound_V_Vials": [],
    "Solaris_Stardust": [],
    "Valyrian_Steel": [],
    "Infinity_Stones": []
}

def current_position_trend(history_list, fast_period=10, slow_period=50):
    if len(history_list) < slow_period:
        return "FLAT"
    fast_ma = sum(history_list[-fast_period:]) / fast_period
    slow_ma = sum(history_list[-slow_period:]) / slow_period
    
    if fast_ma > slow_ma:
        return "LONG"
    elif fast_ma < slow_ma:
        return "SHORT"
    return "FLAT"


def strategy_Heisenberg_Crystals(bar):
    closes = history["Heisenberg_Crystals"]
    closes.append(bar["close"])
    
    period = 20
    if len(closes) < period:
        return "FLAT"
    
    # Calculate SMA and StdDev
    recent_closes = closes[-period:]
    sma = sum(recent_closes) / period
    variance = sum((x - sma) ** 2 for x in recent_closes) / period
    std_dev = math.sqrt(variance)
    
    current_close = bar["close"]
    
    # Mean-Reversion Baseline Rule
    if current_close > sma + (2 * std_dev):
        return "SHORT"
    elif current_close < sma - (2 * std_dev):
        return "LONG"
    
    return "FLAT"


def strategy_Pieces_Of_Eight(bar):
    closes = history["Pieces_Of_Eight"]
    closes.append(bar["close"])
    return current_position_trend(closes)


def strategy_Compound_V_Vials(bar):
    closes = history["Compound_V_Vials"]
    closes.append(bar["close"])
    return current_position_trend(closes)


def strategy_Solaris_Stardust(bar):
    closes = history["Solaris_Stardust"]
    closes.append(bar["close"])
    return current_position_trend(closes)


def strategy_Valyrian_Steel(bar):
    closes = history["Valyrian_Steel"]
    closes.append(bar["close"])
    return current_position_trend(closes)


def strategy_Infinity_Stones(bar):
    closes = history["Infinity_Stones"]
    closes.append(bar["close"])
    return current_position_trend(closes)
