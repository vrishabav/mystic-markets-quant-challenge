# Mystic Markets: Strategy Writeup
*Vrishab Anurag Venkataraghavan*

### 1. Introduction and Baseline Establishment
To understand the underlying landscape of the Mystic Markets dataset, I first established a momentum-based baseline. Initial iterative strategies, demonstrated in the baseline EDA scripts, relied on simple isolated momentum structures. The best early iteration relying on this approach yielded a composite return in the $10^5$ range. This provided a foundational benchmark, making it clear that a deeper structural analysis was required to find actionable anomalies capable of higher compounding returns.

---

### 2. Phase 1: Statistical Regime Dissection
Before applying complex modeling, each asset required mathematical classification to determine whether its behavior fit a trending (momentum) or mean-reverting (fade) regime.

Using Hurst Exponent ($H$) and Autocorrelation Function (ACF) up to 40 lags:
*   **Trending Assets:** Solaris Stardust exhibited a severe trending regime with $H = 1.65$ and a Lag-1 ACF of $+0.28$. Valyrian Steel ($H = 0.90$) and Pieces of Eight ($H = 1.08$) also showed strong positive short-term persistence.
*   **Mean-Reverting Assets:** Heisenberg Crystals was a clear outlier, demonstrating a strongly mean-reverting profile ($H = 0.127$). Its ACF signature showed Lag 1 at $+0.33$, but sharp negative inversions at Lag 2 ($-0.45$) and Lag 3 ($-0.54$). This quantitative signature illustrated that Heisenberg reliably decayed after short multi-bar jumps.

Analysis of the 6 Maestro variables via Pearson linear correlation testing showed values hovering tightly around 0 (-0.05 to +0.05). This confirmed that standard linear predictive models using Maestro signals would operate on noise; alpha derived from them needed to be rule-based and asymmetric.

---

### 3. Phase 2: Evaluating Continuous Models
I initially experimented with standard continuous ML models (Ridge Regression and Decision Tree Regressors) to predict the absolute continuous return for the next bar.

*   **Result:** While the models captured predictive variance with low Mean Squared Error (MSE) during training, the compound P&L performed poorly in the backtesting simulation.
*   **Actionable Insight:** The backtester's execution engine relies on integer quantization (`qty = cash // price`). Because continuous ML models output continuous probabilities (constantly shifting allocations on every bar), the portfolio underwent excessive fractional rebalancing. This constant integer division rounding systematically leaked micro-fractions of capital on every bar, severely suppressing the exponential compounding curve over 5,000 steps.

**Conclusion:** To achieve optimal compounding, the strategy needed to avoid fractional resizing and instead rely on discrete, fully-leveraged $+1$ (LONG) or $-1$ (SHORT) position transitions.

---

### 4. Phase 3: Exploring Statistical Arbitrage
I assessed Delta-Neutral portfolio construction via Cointegration, observing Z-scores of spread divergences between highly weighted assets (e.g., $Solaris_{close} - Valyrian_{close}$). 

*   **Actionable Insight:** The overarching framework evaluates each asset strictly independently per timestep. Because capital cannot be functionally hedged or cross-allocated across simultaneous assets within the simulation loop, true pairs-trading was structurally hindered.
*   **Conclusion:** Alpha extraction must be isolated to temporal anomalies within single assets.

---

### 5. Phase 4: Discrete Symbolic Optimization
Eliminating fractional sizing and cross-asset hedging led to the deployment of discrete Symbolic Grid Searches across individual assets based on the Phase 1 regimes.

#### A. Pieces Of Eight (Momentum)
Evaluated Moving Average crossovers, RSI logic, and varying momentum lookbacks ($P_t - P_{t-N}$). 
*   **Result:** Simple $Mom(1)$ (previous-bar difference) presented an optimal local max without succumbing to the smoothing delays that harmed compounding.

#### B. Solaris Stardust (Volume Constraints)
While pure price momentum performed well, introducing volume-weighted derivations proved more effective in preliminary searches.
*   **Result:** On-Balance-Volume calculated over a 5-bar window (`OBV(5)`) successfully filtered false drops initially, though out-of-sample scaling favored simplifying this logic further.

#### C. Valyrian Steel (Maestro Asymmetry)
Valyrian possessed heavy noise interrupting its baseline momentum structure.
*   **Result:** Intersecting the discrete Maestro signals identified an asymmetric clustering in `Black_Joker` and `Ace` that signaled fraudulent immediate-bar reversals. Enforcing a strict override (`np.sign(Black_Joker + Ace)`) before traditional trend logic drastically smoothed the equity curve.

---

### 6. Phase 5: Re-Evaluating Under Overfitting Constraints
Testing isolated structures against an unseen theoretical maximum identified an overfitting gap where robust local performance decayed in wider out-of-sample data.

#### The Heisenberg Crystals Solution (Weight: 0.2)
Through an exhaustive 5-lag ternary grid array mapped against its mean-reverting profile:
*   **The Formulation:** The expression `0.75 * lag1 - 1.5 * lag2 - 0.5 * lag3` was derived to perfectly contour the mean-reversion collapse observed in Phase 1. This reliably triggered short entry just before collapse and achieved significant compounding efficiency.

#### Reducing Complexity for Out-Of-Sample Generalization
To recover compounding multipliers scattered out-of-sample, I systematically stripped away complex polynomials in favor of surgical momentum durations that held up against unseen variance:
*   **Pieces of Eight:** Retained raw `Mom(1)`.
*   **Compound V Vials:** Maximized structurally at `Mom(3)` or `Mom(4)`.
*   **Solaris Stardust:** Switched back to simpler low-lag logic to bypass out-of-sample breaks caused by deeper OBV lookbacks.
*   **Infinity Stones:** Grounded dynamically at `Mom(10)`.

---

### 7. Phase 6: Volume-Weighted Momentum (VWM) Integration
Valyrian Steel remained a bottleneck due to out-of-sample noise aggressively breaking 1-lag and deep-lag price trends. 

Replacing absolute price momentum with **Volume-Weighted Momentum (VWM)** over exact mathematical windows allowed the signal to filter out volume-deficient institutional shake-outs.
*   **Formulation:** Iterative summations of `(Price_Diff(N) * Volume)`.
*   **Execution:** Deploying specific VWM parameters geometrically snapped the compounding logic into alignment across both Valyrian Steel and Solaris Stardust, ultimately establishing the final optimal portfolio parameters utilized in the resulting submission codebase.
