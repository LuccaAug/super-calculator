from base.base_calculator import BaseCalculator


class Speed(BaseCalculator):
    distance: float
    time: float

    def ask_requirements(self) -> None:
        input_str = input("Enter distance (in meters): ")
        self.distance = float(input_str)

        input_str = input("Enter time (in seconds): ")
        self.time = float(input_str)

    def do_math(self) -> float:
        if self.time == 0:
            raise ValueError("Time can not be 0 to calculate speed.")

        return self.distance / self.time
