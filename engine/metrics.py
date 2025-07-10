import numpy as np

def calculate_returns(equity_curve):
    returns = np.diff(equity_curve) / equity_curve[:-1]
    return returns

def sharpe_ratio(returns, risk_free_rate=0.0):
    excess_returns = returns - risk_free_rate / 252
    return np.sqrt(252) * np.mean(excess_returns) / np.std(excess_returns) if np.std(excess_returns) > 0 else 0

def max_drawdown(equity_curve):
    peak = np.maximum.accumulate(equity_curve)
    drawdown = (equity_curve - peak) / peak
    return np.min(drawdown)

def win_rate(trades):
    wins = [t for t in trades if t['pnl'] > 0]
    return len(wins) / len(trades) if trades else 0.0
