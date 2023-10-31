from base.base_area import BaseArea
from medicine.medicine_calculator import MedicineCalculator
from computation.computation_calculator import ComputationCalculator


class MainMenu:
    options: dict = {
        "C": "Computation",
        "M": "Medicine",
        "E": "Exit",
    }
    calculator_area: BaseArea | None = None
    in_loop: bool = True

    def __init__(self) -> None:
        self.menu_in_loop()
        self.end()

    def reset_variables(self) -> None:
        self.calculator_area = None

    def show_menu(self) -> None:
        print("Choose the area: ")
        for letter, name in self.options:
            print("\t %s - %s" % (letter, name))

    def menu_in_loop(self) -> None:
        while self.in_loop:
            self.reset_variables()
            self.show_menu()

            calculator_type: str = input()
            calculator_type = calculator_type.upper()

            self.define_area(calculator_type)

            if self.calculator_area is None:
                print("Nothing was found, please try again!")
                continue

            self.instantiate_calculator_area()

    def instantiate_calculator_area(self) -> None:
        self.calculator_area.menu()
        self.calculator_area.instantiate_calculator()

    def define_area(self, calculator_type: str):
        if calculator_type == 'E':
            self.in_loop = False
            return

        elif calculator_type == 'M':
            self.calculator_area = MedicineCalculator()

        elif calculator_type == 'C':
            self.calculator_area = ComputationCalculator()

    def end(self):
        print("Thanks for using the super-calculator! :D")


if __name__ == "__main__":
    MainMenu()
