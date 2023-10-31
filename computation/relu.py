from base.base_calculator import BaseCalculator


class ReLU(BaseCalculator):
    input: float

    def ask_requirements(self) -> None:
        input_str = input("Input: ")
        self.input = float(input_str)

    def do_math(self) -> float:
        if self.input < 0:
            return 0

        return self.input
