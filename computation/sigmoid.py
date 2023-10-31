from base.base_calculator import BaseCalculator

from math import pow, e


class Sigmoid(BaseCalculator):
    input: float

    def ask_requirements(self) -> None:
        input_str = input("Input: ")
        self.input = float(input_str)

    def do_math(self) -> float:
        euler = pow(e, -self.input)
        sum = 1 + euler
        return 1/sum
