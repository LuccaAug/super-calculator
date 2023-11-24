from base.base_area import BaseArea
from medicine.medicine_calculator import MedicineCalculator
from computation.computation_calculator import ComputationCalculator
from physic.physic_calculator import PhysicCalculator
from trigonometric.trigonometric_calculator import TrigonometricCalculator

options: dict = {
    "C": "Computation",
    "M": "Medicine",
    "P": "Physic",
    "T": "Trigonometric",
    "E": "Exit",
}


class MainMenu:
    options: dict = {
        "C": "Computation",
        "M": "Medicine",
        "P": "Physic",
        "T": "Trigonometric",
        "E": "Exit",
    }
    calculator_area: BaseArea | None = None
    in_loop: bool = True

    def reset_variables(self) -> None:
        self.calculator_area = None

    def show_menu(self) -> None:
        print("Choose the area: ")
        for letter, name in self.options.items():
            print("\t %s - %s" % (letter, name))

    def menu_in_loop(self) -> None:
        while self.in_loop:
            self.reset_variables()
            self.show_menu()

            calculator_type: str = input()
            calculator_type = calculator_type.upper()

            self.define_area(calculator_type)
            if not self.in_loop:
                break

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

        elif calculator_type == 'P':
            self.calculator_area = PhysicCalculator()

        elif calculator_type == 'T':
            self.calculator_area = TrigonometricCalculator()

    def end(self) -> None:
        print("Thanks for using the super-calculator! :D")


if __name__ == "__main__":
    menu = MainMenu()

    menu.menu_in_loop()
    menu.end()
