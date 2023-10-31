from base.base_calculator import BaseCalculator

from math import tanh


class TanH(BaseCalculator):
    input: float

    def ask_requirements(self) -> None:
        input_str = input("Input: ")
        self.input = float(input_str)

    def do_math(self) -> float:
        return tanh(self.input)
