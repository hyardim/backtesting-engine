import pandas as pd

class BaseStrategy:
    """
    Base class for all trading strategies.
    Each strategy should implement the generate_signal method.
    """
    def generate_signal(self, row):
        raise NotImplementedError("generate_signal must be implemented by the strategy.")

class SMACrossoverStrategy(BaseStrategy):
    """
    Simple Moving Average (SMA) Crossover Strategy:
    - Buys when the short-term SMA crosses above the long-term SMA.
    - Sells when the short-term SMA crosses below the long-term SMA.
    - Holds otherwise.
    """
    def __init__(self, short_window=20, long_window=50):
        self.short_window = short_window
        self.long_window = long_window
        self.prices = []
    def generate_signal(self, row):
        # Append the latest closing price
        self.prices.append(row['Close'])
        # Wait until enough data is available for both SMAs
        if len(self.prices) < self.long_window:
            return 0  # Hold
        # Calculate short and long SMAs
        short_ma = pd.Series(self.prices[-self.short_window:]).mean()
        long_ma = pd.Series(self.prices[-self.long_window:]).mean()
        # Generate trading signals
        if short_ma > long_ma:
            return 1   # Buy
        elif short_ma < long_ma:
            return -1  # Sell
        else:
            return 0   # Hold

class BuyAndHoldStrategy(BaseStrategy):
    """
    Buy and Hold Strategy:
    - Buys at the first opportunity and holds the position.
    """
    def __init__(self):
        self.has_bought = False
    def generate_signal(self, row):
        if not self.has_bought:
            self.has_bought = True
            return 1  # Buy
        return 0      # Hold
