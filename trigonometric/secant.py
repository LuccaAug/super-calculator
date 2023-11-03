from base.base_calculator import BaseCalculator
import math


class Secant(BaseCalculator):
    angle_degrees: float

    def ask_requirements(self) -> None:
        input_str = input("Enter angle in degrees: ")
        self.angle_degrees = float(input_str)

    def do_math(self) -> float:
        self.angle_degrees = self.angle_degrees % 360

        if self.angle_degrees in [-270, -90, 90, 270]:
            raise ValueError("Secant is undefined for this angle.")

        radians = math.radians(self.angle_degrees)
        cosine_value = math.cos(radians)

        secant_value = 1 / cosine_value

        return round(secant_value, 2)
