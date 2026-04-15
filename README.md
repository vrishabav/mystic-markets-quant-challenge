# Mystic Markets: Quant Trading Algorithm

This repository contains the end-to-end quantitative analysis and algorithmic trading strategy developed for the "Mystic Markets" multi-asset dataset. The strategy achieved significant exponential compounding through discrete, volume-weighted momentum optimizations and precise constraint formulation.

## Competition Overview & Requirements

The strategy was developed for a trading simulation challenge involving 6 distinct, anonymized assets provided in a single timeline-aligned CSV dataset:
*   Heisenberg Crystals
*   Pieces Of Eight
*   Compound V Vials
*   Solaris Stardust
*   Valyrian Steel
*   Infinity Stones

### Rules and Mechanics:
*   **Independent Strategies:** A discrete trading function must evaluate each asset row-by-row.
*   **Capital & Positions:** Each asset starts with a decoupled, independent ₹10,000 allocation. Strategies can only hold one directional position per asset at any time: `LONG`, `SHORT`, or `FLAT`. 
*   **Execution:** All orders mathematically execute at the bar's `close` price without fractional share sizes. The simulation rounds purely to integers (`qty = cash // price`).
*   **Features:** In addition to standard OHLCV tick data, six discrete "Maestro" signals (Jack, Queen, Red_Joker, Ace, Black_Joker, King) indicate underlying categorical, potentially fraudulent, shifts across the data.
*   **Scoring Metric:** The final portfolio is an aggregated, weighted net PnL sum across the 6 assets.

## Repository Structure

- `strategy_writeup.md`: Detailed breakdown of the statistical analysis, mathematical modeling, and iterative improvements that led to the final logic.
- `src/`: 
  - `strategy_final.py`: The final executed Python trading algorithm.
  - `backtester/`: The local simulation and execution engine (`runner.py`, `backtester.py`) to evaluate the strategy isolated per asset.
  - `experiments/`: Select intermediate iterations showcasing the progression from basic moving average crossovers to complex Volume-Weighted-Momentum integration.
- `dataset.csv`: The underlying price and volume market data.

## Usage

Create a virtual environment and install the required dependencies (numpy, pandas, scipy). 

Run the backtester against the main strategy file:
```bash
python src/backtester/runner.py dataset.csv src/strategy_final.py
```

## Strategy Highlights

*   **Asset Categorization:** Rigorously separated the heavily trending assets (Solaris Stardust, Valyrian Steel) from mean-reverting outliers (Heisenberg Crystals) using Hurst Exponents and Autocorrelation analysis.
*   **Avoidance of Fractional Allocation:** Replaced continuous ML probability allocations with discrete state definitions (LONG/SHORT) to prevent continuous integer-division leakages during the backtest compounding loop.
*   **Volume-Weighted Momentum (VWM):** Applied VWM envelopes specifically across high-volatility trending assets to filter institutional shake-outs and lock in exponential compound growth.
