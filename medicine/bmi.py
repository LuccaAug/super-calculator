from base.base_calculator import BaseCalculator


class BMI(BaseCalculator):
    weight: float
    height: float

    def ask_requirements(self) -> None:
        height_str = input("Height (meters): ")
        self.height = float(height_str)

        weight_str = input("Weight (kilograms): ")
        self.weight = float(weight_str)

    def do_math(self) -> float:
        height_square = self.height * self.height
        imc = self.weight / height_square
        return round(imc, 2)
