from engine.data_handler import DataHandler
from engine.portfolio import Portfolio
from engine.execution import ExecutionHandler
from engine.backtester import Backtester
from strategies.sma_crossover import SMACrossoverStrategy

if __name__ == '__main__':
    data_handler = DataHandler('data/sample_data.csv')
    strategy = SMACrossoverStrategy(short_window=5, long_window=20)
    portfolio = Portfolio(initial_cash=100000)
    execution_handler = ExecutionHandler()
    backtester = Backtester(data_handler, strategy, portfolio, execution_handler)
    metrics, equity_curve = backtester.run()
    print('Backtest Metrics:')
    for k, v in metrics.items():
        print(f'{k}: {v:.2%}' if isinstance(v, float) else f'{k}: {v}')
