
import numpy as np

# Weights extracted from L2-Regularized Autoregressive Machine Learning

# Model for Compound_V_Vials
def strategy_Compound_V_Vials(bar, _state={'closes': []}):
    c = float(bar['close'])
    _state['closes'].append(c)
    if len(_state['closes']) > 11:
        _state['closes'].pop(0)
    if len(_state['closes']) < 11:
        return 'FLAT'

    pred = 0.000022
    pred += 0.000454 * ((c / _state['closes'][-(1 + 1)]) - 1.0)
    pred += 0.000857 * ((c / _state['closes'][-(1 + 2)]) - 1.0)
    pred += 0.001171 * ((c / _state['closes'][-(1 + 3)]) - 1.0)
    pred += 0.001403 * ((c / _state['closes'][-(1 + 4)]) - 1.0)
    pred += 0.001357 * ((c / _state['closes'][-(1 + 5)]) - 1.0)
    pred += 0.001334 * ((c / _state['closes'][-(1 + 6)]) - 1.0)
    pred += 0.001296 * ((c / _state['closes'][-(1 + 7)]) - 1.0)
    pred += 0.001271 * ((c / _state['closes'][-(1 + 8)]) - 1.0)
    pred += 0.001210 * ((c / _state['closes'][-(1 + 9)]) - 1.0)
    pred += 0.001131 * ((c / _state['closes'][-(1 + 10)]) - 1.0)
    pred += 0.000104 * float(bar.get('King', 0))

    if pred > 0:
        return 'LONG'
    elif pred < 0:
        return 'SHORT'
    return 'FLAT'


# Model for Heisenberg_Crystals
def strategy_Heisenberg_Crystals(bar, _state={'closes': []}):
    c = float(bar['close'])
    _state['closes'].append(c)
    if len(_state['closes']) > 11:
        _state['closes'].pop(0)
    if len(_state['closes']) < 11:
        return 'FLAT'

    pred = 0.000004
    pred += 0.000232 * ((c / _state['closes'][-(1 + 1)]) - 1.0)
    pred += -0.000462 * ((c / _state['closes'][-(1 + 3)]) - 1.0)
    pred += -0.000636 * ((c / _state['closes'][-(1 + 4)]) - 1.0)
    pred += -0.000490 * ((c / _state['closes'][-(1 + 5)]) - 1.0)
    pred += -0.000216 * ((c / _state['closes'][-(1 + 6)]) - 1.0)
    pred += -0.000193 * ((c / _state['closes'][-(1 + 8)]) - 1.0)
    pred += -0.000376 * ((c / _state['closes'][-(1 + 9)]) - 1.0)
    pred += -0.000472 * ((c / _state['closes'][-(1 + 10)]) - 1.0)
    pred += 0.000347 * float(bar.get('Queen', 0))
    pred += 0.000172 * float(bar.get('Red_Joker', 0))
    pred += 0.000137 * float(bar.get('Ace', 0))
    pred += -0.000159 * float(bar.get('Black_Joker', 0))

    if pred > 0:
        return 'LONG'
    elif pred < 0:
        return 'SHORT'
    return 'FLAT'


# Model for Infinity_Stones
def strategy_Infinity_Stones(bar, _state={'closes': []}):
    c = float(bar['close'])
    _state['closes'].append(c)
    if len(_state['closes']) > 11:
        _state['closes'].pop(0)
    if len(_state['closes']) < 11:
        return 'FLAT'

    pred = 0.000190
    pred += 0.000469 * ((c / _state['closes'][-(1 + 1)]) - 1.0)
    pred += 0.000446 * ((c / _state['closes'][-(1 + 2)]) - 1.0)
    pred += 0.000940 * ((c / _state['closes'][-(1 + 3)]) - 1.0)
    pred += 0.001342 * ((c / _state['closes'][-(1 + 4)]) - 1.0)
    pred += 0.001241 * ((c / _state['closes'][-(1 + 5)]) - 1.0)
    pred += 0.001375 * ((c / _state['closes'][-(1 + 6)]) - 1.0)
    pred += 0.001217 * ((c / _state['closes'][-(1 + 7)]) - 1.0)
    pred += 0.001248 * ((c / _state['closes'][-(1 + 8)]) - 1.0)
    pred += 0.001011 * ((c / _state['closes'][-(1 + 9)]) - 1.0)
    pred += 0.000791 * ((c / _state['closes'][-(1 + 10)]) - 1.0)
    pred += 0.000182 * float(bar.get('Jack', 0))
    pred += 0.001056 * float(bar.get('Queen', 0))
    pred += 0.000775 * float(bar.get('Red_Joker', 0))
    pred += 0.000745 * float(bar.get('Ace', 0))
    pred += 0.000553 * float(bar.get('Black_Joker', 0))
    pred += -0.001351 * float(bar.get('King', 0))

    if pred > 0:
        return 'LONG'
    elif pred < 0:
        return 'SHORT'
    return 'FLAT'


# Model for Pieces_Of_Eight
def strategy_Pieces_Of_Eight(bar, _state={'closes': []}):
    c = float(bar['close'])
    _state['closes'].append(c)
    if len(_state['closes']) > 11:
        _state['closes'].pop(0)
    if len(_state['closes']) < 11:
        return 'FLAT'

    pred = -0.000001
    pred += 0.000301 * ((c / _state['closes'][-(1 + 1)]) - 1.0)
    pred += 0.000308 * ((c / _state['closes'][-(1 + 2)]) - 1.0)
    pred += 0.000335 * ((c / _state['closes'][-(1 + 3)]) - 1.0)
    pred += 0.000298 * ((c / _state['closes'][-(1 + 4)]) - 1.0)
    pred += 0.000305 * ((c / _state['closes'][-(1 + 5)]) - 1.0)
    pred += 0.000372 * ((c / _state['closes'][-(1 + 6)]) - 1.0)
    pred += 0.000359 * ((c / _state['closes'][-(1 + 7)]) - 1.0)
    pred += 0.000389 * ((c / _state['closes'][-(1 + 8)]) - 1.0)
    pred += 0.000406 * ((c / _state['closes'][-(1 + 9)]) - 1.0)
    pred += 0.000400 * ((c / _state['closes'][-(1 + 10)]) - 1.0)
    pred += 0.000285 * float(bar.get('Jack', 0))
    pred += -0.000500 * float(bar.get('Queen', 0))
    pred += -0.000195 * float(bar.get('Red_Joker', 0))
    pred += 0.000114 * float(bar.get('Black_Joker', 0))
    pred += 0.000102 * float(bar.get('King', 0))

    if pred > 0:
        return 'LONG'
    elif pred < 0:
        return 'SHORT'
    return 'FLAT'


# Model for Solaris_Stardust
def strategy_Solaris_Stardust(bar, _state={'closes': []}):
    c = float(bar['close'])
    _state['closes'].append(c)
    if len(_state['closes']) > 11:
        _state['closes'].pop(0)
    if len(_state['closes']) < 11:
        return 'FLAT'

    pred = 0.000061
    pred += 0.000147 * ((c / _state['closes'][-(1 + 1)]) - 1.0)
    pred += 0.000292 * ((c / _state['closes'][-(1 + 2)]) - 1.0)
    pred += 0.000439 * ((c / _state['closes'][-(1 + 3)]) - 1.0)
    pred += 0.000608 * ((c / _state['closes'][-(1 + 4)]) - 1.0)
    pred += 0.000740 * ((c / _state['closes'][-(1 + 5)]) - 1.0)
    pred += 0.000874 * ((c / _state['closes'][-(1 + 6)]) - 1.0)
    pred += 0.000980 * ((c / _state['closes'][-(1 + 7)]) - 1.0)
    pred += 0.001093 * ((c / _state['closes'][-(1 + 8)]) - 1.0)
    pred += 0.001205 * ((c / _state['closes'][-(1 + 9)]) - 1.0)
    pred += 0.001317 * ((c / _state['closes'][-(1 + 10)]) - 1.0)
    pred += 0.000288 * float(bar.get('King', 0))

    if pred > 0:
        return 'LONG'
    elif pred < 0:
        return 'SHORT'
    return 'FLAT'


# Model for Valyrian_Steel
def strategy_Valyrian_Steel(bar, _state={'closes': []}):
    c = float(bar['close'])
    _state['closes'].append(c)
    if len(_state['closes']) > 11:
        _state['closes'].pop(0)
    if len(_state['closes']) < 11:
        return 'FLAT'

    pred = 0.000061
    pred += 0.000495 * ((c / _state['closes'][-(1 + 1)]) - 1.0)
    pred += 0.000929 * ((c / _state['closes'][-(1 + 2)]) - 1.0)
    pred += 0.001252 * ((c / _state['closes'][-(1 + 3)]) - 1.0)
    pred += 0.001085 * ((c / _state['closes'][-(1 + 4)]) - 1.0)
    pred += 0.000996 * ((c / _state['closes'][-(1 + 5)]) - 1.0)
    pred += 0.000656 * ((c / _state['closes'][-(1 + 6)]) - 1.0)
    pred += 0.000460 * ((c / _state['closes'][-(1 + 7)]) - 1.0)
    pred += 0.000341 * ((c / _state['closes'][-(1 + 8)]) - 1.0)
    pred += 0.000594 * float(bar.get('Jack', 0))
    pred += 0.000196 * float(bar.get('Queen', 0))
    pred += -0.000437 * float(bar.get('Red_Joker', 0))
    pred += 0.000914 * float(bar.get('Ace', 0))
    pred += 0.001256 * float(bar.get('Black_Joker', 0))
    pred += 0.000228 * float(bar.get('King', 0))

    if pred > 0:
        return 'LONG'
    elif pred < 0:
        return 'SHORT'
    return 'FLAT'

