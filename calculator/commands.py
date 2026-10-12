from calculator.calculation import Calculation


class CalculateCommand:
    def __init__(self, calculation: Calculation, history: list):
        self.calculation = calculation
        self.history = history

    def execute(self):
        result = self.calculation.execute()
        self.history.append(
            f"{self.calculation.a:g} "
            f"{self.calculation.operation.__name__} "
            f"{self.calculation.b:g} = {result:g}"
        )
        return result


class HistoryCommand:
    def __init__(self, history: list):
        self.history = history

    def execute(self):
        return self.history.copy()
