from base.base_calculator import BaseCalculator


class Acceleration(BaseCalculator):
    initial_velocity: float
    final_velocity: float
    time: float

    def ask_requirements(self) -> None:
        input_str = input("Enter initial velocity (in m/s): ")
        self.initial_velocity = float(input_str)

        input_str = input("Enter final velocity (m/s): ")
        self.final_velocity = float(input_str)

        input_str = input("Enter time (in seconds): ")
        self.time = float(input_str)

    def do_math(self) -> float:
        if self.time == 0:
            raise ValueError("Time can not be 0 to calculate acceleration.")

        acceleration = (self.final_velocity - self.initial_velocity) / self.time

        return round(acceleration, 2)
