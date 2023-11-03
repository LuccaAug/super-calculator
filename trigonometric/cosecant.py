from base.base_calculator import BaseCalculator
import math


class Cosecant(BaseCalculator):
    angle_degrees: float

    def ask_requirements(self) -> None:
        input_str = input("Enter angle in degrees: ")
        self.angle_degrees = float(input_str)

    def do_math(self) -> float:
        self.angle_degrees = self.angle_degrees % 360

        if self.angle_degrees in [-180, 0, 180]:
            raise ValueError("Cosecant is undefined for this angle.")

        radians = math.radians(self.angle_degrees)
        sine_value = math.sin(radians)

        cosecant_value = 1 / sine_value

        return round(cosecant_value, 2)
