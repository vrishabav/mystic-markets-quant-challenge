
import numpy as np

def strategy_Heisenberg_Crystals(bar, _state={"c": []}):
    _state["c"].append(float(bar["close"]))
    if len(_state["c"]) > 6: _state["c"].pop(0)
    if len(_state["c"]) < 6: return "FLAT"

    # 0_-1_0_-0.5_0 => -1.0 * lag2 - 0.5 * lag4
    lag2 = _state["c"][-2] - _state["c"][-3]
    lag4 = _state["c"][-4] - _state["c"][-5]

    val = -1.0 * lag2 - 0.5 * lag4
    return "LONG" if val > 0 else "SHORT"

def strategy_Pieces_Of_Eight(bar, _state={"c": []}):
    _state["c"].append(float(bar["close"]))
    if len(_state["c"]) > 2: _state["c"].pop(0)
    if len(_state["c"]) < 2: return "FLAT"
    diff = _state["c"][-1] - _state["c"][0]
    return "LONG" if diff > 0 else ("SHORT" if diff < 0 else "FLAT")

def strategy_Compound_V_Vials(bar, _state={"c": []}):
    _state["c"].append(float(bar["close"]))
    if len(_state["c"]) > 4: _state["c"].pop(0)
    if len(_state["c"]) < 4: return "FLAT"

    # linear_1_0.5_0 => lag1 + 0.5 * lag2
    lag1 = _state["c"][-1] - _state["c"][-2]
    lag2 = _state["c"][-2] - _state["c"][-3]
    val = lag1 + 0.5 * lag2

    if val > 0: return "LONG"
    elif val < 0: return "SHORT"
    return "FLAT"

def strategy_Solaris_Stardust(bar, _s={'c': [], 'obv': 0, 'obv_hist': []}):
    c = float(bar['close'])
    v = float(bar['volume'])
    _s['c'].append(c)
    if len(_s['c']) > 2: _s['c'].pop(0)

    if len(_s['c']) == 2:
        if _s['c'][-1] > _s['c'][0]: _s['obv'] += v
        elif _s['c'][-1] < _s['c'][0]: _s['obv'] -= v

    _s['obv_hist'].append(_s['obv'])
    if len(_s['obv_hist']) > 6: _s['obv_hist'].pop(0)  # OBV(5) requires 6 states
    if len(_s['obv_hist']) < 6: return "FLAT"

    diff = _s['obv_hist'][-1] - _s['obv_hist'][0]
    return "LONG" if diff > 0 else ("SHORT" if diff < 0 else "FLAT")

def strategy_Valyrian_Steel(bar, _s={"c": []}):
    _s["c"].append(float(bar["close"]))
    if len(_s["c"]) > 4: _s["c"].pop(0)
    if len(_s["c"]) < 4: return "FLAT"

    bj = float(bar.get("Black_Joker", 0))
    ace = float(bar.get("Ace", 0))
    vote = np.sign(bj + ace)
    if vote > 0: return "LONG"
    elif vote < 0: return "SHORT"

    diff = _s["c"][-1] - _s["c"][0]
    return "LONG" if diff > 0 else ("SHORT" if diff < 0 else "FLAT")

def strategy_Infinity_Stones(bar, _s={"c": []}):
    _s["c"].append(float(bar["close"]))
    if len(_s["c"]) > 7: _s["c"].pop(0)
    if len(_s["c"]) < 7: return "FLAT"

    diff = _s["c"][-1] - _s["c"][0]
    return "LONG" if diff > 0 else ("SHORT" if diff < 0 else "FLAT")

