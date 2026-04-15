"""
Iteration 7: Valyrian Mom(8) & Solaris Mom(2)
Testing shifted momentum lookback windows for Valyrian and Solaris based on local optima.
"""
def strategy_Heisenberg_Crystals(bar, _s={"c": []}):
    _s["c"].append(float(bar["close"]))
    if len(_s["c"]) > 5: _s["c"].pop(0)
    if len(_s["c"]) < 5: return "FLAT"
    val = 0.75 * (_s["c"][-1] - _s["c"][-2]) - 1.5 * (_s["c"][-2] - _s["c"][-3]) - 0.5 * (_s["c"][-3] - _s["c"][-4])
    return "LONG" if val > 0 else "SHORT"

def strategy_Pieces_Of_Eight(bar, _s={"c": []}):
    _s["c"].append(float(bar["close"]))
    if len(_s["c"]) > 2: _s["c"].pop(0)
    if len(_s["c"]) < 2: return "FLAT"
    diff = _s["c"][-1] - _s["c"][0] # Mom(1)
    return "LONG" if diff > 0 else ("SHORT" if diff < 0 else "FLAT")

def strategy_Compound_V_Vials(bar, _s={"c": []}):
    _s["c"].append(float(bar["close"]))
    if len(_s["c"]) > 5: _s["c"].pop(0)
    if len(_s["c"]) < 5: return "FLAT"
    diff = _s["c"][-1] - _s["c"][0] # Mom(4)
    return "LONG" if diff > 0 else ("SHORT" if diff < 0 else "FLAT")

def strategy_Solaris_Stardust(bar, _s={"c": []}):
    _s["c"].append(float(bar["close"]))
    if len(_s["c"]) > 3: _s["c"].pop(0)
    if len(_s["c"]) < 3: return "FLAT"
    diff = _s["c"][-1] - _s["c"][0] # Mom(2)
    return "LONG" if diff > 0 else ("SHORT" if diff < 0 else "FLAT")

def strategy_Valyrian_Steel(bar, _s={"c": []}):
    _s["c"].append(float(bar["close"]))
    if len(_s["c"]) > 9: _s["c"].pop(0)
    if len(_s["c"]) < 9: return "FLAT"
    diff = _s["c"][-1] - _s["c"][0] # Mom(8)
    return "LONG" if diff > 0 else ("SHORT" if diff < 0 else "FLAT")

def strategy_Infinity_Stones(bar, _s={"c": []}):
    _s["c"].append(float(bar["close"]))
    if len(_s["c"]) > 8: _s["c"].pop(0)
    if len(_s["c"]) < 8: return "FLAT"
    diff = _s["c"][-1] - _s["c"][0] # Mom(7)
    return "LONG" if diff > 0 else ("SHORT" if diff < 0 else "FLAT")
