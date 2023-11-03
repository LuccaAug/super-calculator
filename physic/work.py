from base.base_calculator import BaseCalculator


class Work(BaseCalculator):
    force: float
    distance: float

    def ask_requirements(self) -> None:
        input_str = input("Enter force (in newtons): ")
        self.force = float(input_str)

        input_str = input("Enter distance (in meters): ")
        self.distance = float(input_str)

    def do_math(self) -> float:
        work = self.force * self.distance

        return round(work, 2)
