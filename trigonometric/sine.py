from base.base_calculator import BaseCalculator
import math


class Sine(BaseCalculator):
    angle_degrees: float

    def ask_requirements(self) -> None:
        input_str = input("Enter angle in degrees: ")
        self.angle_degrees = float(input_str)

    def do_math(self) -> float:
        radians = math.radians(self.angle_degrees)
        sine_value = math.sin(radians)

        return round(sine_value, 2)
