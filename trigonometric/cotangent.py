from base.base_calculator import BaseCalculator
import math


class Cotangent(BaseCalculator):
    angle_degrees: float

    def ask_requirements(self) -> None:
        input_str = input("Enter angle in degrees: ")
        self.angle_degrees = float(input_str)

    def do_math(self) -> float:
        self.angle_degrees = self.angle_degrees % 360

        if self.angle_degrees in [-180, 0, 180]:
            raise ValueError("Cotangent is undefined for this angle.")

        radians = math.radians(self.angle_degrees)
        tangent_value = math.tan(radians)
        cotangent_value = 1 / tangent_value

        return round(cotangent_value, 2)
