class StockSpanner:

    def __init__(self):
        self.prices = []
        self.spans = []

    def next_day_span(self, price):
        span = 1
        while self.prices and self.prices[-1] <= price:
            span += self.spans.pop()
            self.prices.pop()
        self.prices.append(price)
        self.spans.append(span)
        return span

# Example usage:
spanner = StockSpanner()
print(spanner.next_day_span(100))  # Output: 1
print(spanner.next_day_span(80))   # Output: 1
print(spanner.next_day_span(60))   # Output: 1
print(spanner.next_day_span(70))   # Output: 2
print(spanner.next_day_span(60))   # Output: 1
print(spanner.next_day_span(75))   # Output: 4
print(spanner.next_day_span(85))   # Output: 6
