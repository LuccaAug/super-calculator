from base.base_calculator import BaseCalculator

import math


class TanH(BaseCalculator):
    input: float

    def ask_requirements(self) -> None:
        input_str = input("Input: ")
        self.input = float(input_str)

    def do_math(self) -> float:
        tanh = math.tanh(self.input)

        return round(tanh, 2)
