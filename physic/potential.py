from base.base_calculator import BaseCalculator


class Potential(BaseCalculator):
    mass: float
    height: float
    potential_energy: float

    def ask_requirements(self) -> None:
        input_str = input("Enter mass (in kg): ")
        self.mass = float(input_str)

        input_str = input("Enter height (in meters): ")
        self.height = float(input_str)

    def do_math(self) -> float:
        gravitational_constant = 9.81  # Acceleration due to gravity (m/s^2)
        self.potential_energy = gravitational_constant * self.mass * self.height
        return self.potential_energy
