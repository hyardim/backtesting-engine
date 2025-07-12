from engine.metrics import calculate_returns, sharpe_ratio, max_drawdown, win_rate, sortino_ratio, calmar_ratio

class Backtester:
    def __init__(self, data_handler, strategy, portfolio, execution_handler):
        self.data_handler = data_handler
        self.strategy = strategy
        self.portfolio = portfolio
        self.execution_handler = execution_handler
        self.trades = []
    def run(self):
        data = self.data_handler.get_data()
        for date, row in data.iterrows():
            price = row['close']  # Changed from 'Close' to 'close'
            signal = self.strategy.generate_signal(row)
            executed_signal = self.execution_handler.execute_order(signal)
            prev_equity = self.portfolio.cash + self.portfolio.position * price
            self.portfolio.update(price, executed_signal)
            new_equity = self.portfolio.cash + self.portfolio.position * price
            if executed_signal != 0:
                self.trades.append({'date': date, 'pnl': new_equity - prev_equity})
        equity_curve = self.portfolio.get_equity_curve()
        returns = calculate_returns(equity_curve)
        metrics = {
            'Total Return': equity_curve[-1] / equity_curve[0] - 1,
            'Sharpe Ratio': sharpe_ratio(returns),
            'Max Drawdown': max_drawdown(equity_curve),
            'Win Rate': win_rate(self.trades),
            'Sortino Ratio': sortino_ratio(returns),
            'Calmar Ratio': calmar_ratio(returns, equity_curve)
        }
        return metrics, equity_curve
