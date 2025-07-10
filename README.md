# Backtesting Engine

A modular Python backtesting engine for quantitative trading strategies.

## Features
- Modular design (data, strategy, portfolio, execution, metrics)
- Example SMA crossover strategy
- Easily extensible for new strategies and metrics

## Getting Started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Add your historical data to the `data/` folder (see `sample_data.csv` format).
3. Run the backtest:
   ```bash
   python main.py
   ```

## File Structure
- `engine/`: Core engine modules
- `strategies/`: Trading strategies
- `data/`: Historical data
- `results/`: Output/results

## Example Output
```
Backtest Metrics:
Total Return: 12.34%
Sharpe Ratio: 1.23
Max Drawdown: -5.67%
Win Rate: 0.45
```
