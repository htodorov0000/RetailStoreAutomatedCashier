class Cash():
    """Physical currency - bills and coins."""
    def __init__(self, value):
        self.value = value
        if self.value < 1:
            self.name = "c" + str(value * 100)
        else:
            self.name = "E" + str(value)

def make_currency():
    values = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100]
    units = []
    for value in values:
        units.append(Cash(value))
    return units

currency_units = make_currency()
currency_units.reverse()