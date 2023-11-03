from base.base_calculator import BaseCalculator


class Gravitation(BaseCalculator):
    mass1: float
    mass2: float
    distance: float

    def ask_requirements(self) -> None:
        input_str = float(input("Enter mass of object 1 (in kg): "))
        self.mass1 = float(input_str)

        input_str = float(input("Enter mass of object 2 (in kg): "))
        self.mass2 = float(input_str)

        input_str = float(input("Enter distance (in meters): "))
        self.distance = float(input_str)

    def do_math(self) -> float:
        gravitational_constant = 6.67e-11  # Gravitational constant (m^3/kg/s^2)

        if self.distance == 0:
            raise ValueError("Distance can not be 0 to calculate gravitational force.")

        return (gravitational_constant * self.mass1 * self.mass2) / (self.distance ** 2)
