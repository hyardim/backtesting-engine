class Portfolio:
    def __init__(self, initial_cash=100000):
        self.initial_cash = initial_cash
        self.cash = initial_cash
        self.position = 0
        self.equity_curve = []
    def update(self, price, signal):
        # Simple logic: buy/sell all-in
        if signal == 1 and self.position == 0:
            self.position = self.cash / price
            self.cash = 0
        elif signal == -1 and self.position > 0:
            self.cash = self.position * price
            self.position = 0
        self.equity_curve.append(self.cash + self.position * price)
    def get_equity_curve(self):
        return self.equity_curve
