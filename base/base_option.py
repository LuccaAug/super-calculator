from base.base_calculator import BaseCalculator


class BaseOption:
    name: str
    calculator: BaseCalculator

    def __init__(self, name: str, calculator: BaseCalculator) -> None:
        self.name = name
        self.calculator = calculator
