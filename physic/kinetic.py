from base.base_calculator import BaseCalculator


class Kinetic(BaseCalculator):
    mass: float
    velocity: float
    kinetic_energy: float

    def ask_requirements(self) -> None:
        input_str = input("Enter mass (in kg): ")
        self.mass = float(input_str)

        input_str = input("Enter velocity (in m/s): ")
        self.velocity = float(input_str)

    def do_math(self) -> float:
        self.kinetic_energy = 0.5 * self.mass * (self.velocity ** 2)
        return self.kinetic_energy
