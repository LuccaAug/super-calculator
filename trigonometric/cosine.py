from base.base_calculator import BaseCalculator
import math


class Cosine(BaseCalculator):
    angle_degrees: float

    def ask_requirements(self) -> None:
        input_str = input("Enter angle in degrees: ")
        self.angle_degrees = float(input_str)

    def do_math(self) -> float:
        radians = math.radians(self.angle_degrees)
        cosine_value = math.cos(radians)

        return round(cosine_value, 2)
