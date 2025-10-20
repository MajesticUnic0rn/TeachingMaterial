# Time Series Analysis Tutorial

An interactive introduction to time series analysis with Plotly visualizations!

## 📚 What You'll Learn

This tutorial covers essential time series concepts through interactive visualizations:

1. **Basic Time Series Visualization** - Understanding trends, seasonality, and noise
2. **Heteroscedasticity** - How variance changes over time
3. **Autocorrelation (ACF)** - Measuring self-correlation at different lags
4. **Partial Autocorrelation (PACF)** - Direct correlations between observations
5. **ARIMA Models** - Introduction to forecasting with ARIMA
6. **Model Diagnostics** - Evaluating model performance

## 🚀 Getting Started

### Installation

1. Install dependencies using uv (recommended):

```bash
uv pip install -e .
```

Or using pip:

```bash
pip install -e .
```

2. Launch Jupyter:

```bash
jupyter notebook intro-timeseries.ipynb
```

Or use Jupyter Lab:

```bash
jupyter lab intro-timeseries.ipynb
```

## 📖 Key Concepts

### Stationarity

A stationary series has a constant mean, variance, and autocorrelation over time.

**Why do we care about stationary series?**

- Makes patterns consistent and predictable
- Most classical models like ARIMA, ARMA, SARIMA rely on stationarity
- Their formulas assume that past behavior (autocorrelations) can be used to model future behavior

After removing trends and seasonality (via differencing, detrending, or decomposition), we can model the underlying "signal" accurately.

You want to make the line predictable. Not necessarily flat.

### What if you can't make it stationary?

- Use other models like **SARIMAX** (adding exogenous variables)
- Try **Prophet** for time series with seasonality (holidays, weekdays, etc.)
- For highly non-stationary data, try tree-based models like **Random Forest** or **Gradient Boosting**
  - Note: You'll need to add lags as features and time-based features

## 🎯 Interactive Features

The notebook includes:

- **Interactive Plotly charts** - Hover, zoom, and explore the data
- **Hands-on experiments** - Modify parameters and see results in real-time
- **Practice exercises** - Test your understanding
- **Real-world examples** - Learn with practical scenarios

## 📊 Topics Covered

1. Time series decomposition (trend + seasonality + noise)
2. Homoscedasticity vs Heteroscedasticity visualization
3. Rolling variance analysis
4. ACF and PACF plots with confidence intervals
5. ARIMA model fitting and forecasting
6. Residual diagnostics (Q-Q plots, ACF of residuals)
7. Model evaluation metrics (MAE, RMSE)

## 🧑‍🎓 For Students

Work through the notebook sequentially. Each section builds on previous concepts. Don't hesitate to modify the code and experiment with different parameters!

**Practice Exercises** are included at the end to reinforce learning.

## 📚 Further Learning

- **SARIMA**: Seasonal ARIMA models
- **VAR**: Vector AutoRegression for multivariate series
- **Prophet**: Facebook's forecasting library
- **LSTM**: Deep learning approaches for time series

---

Happy Learning! 📈
