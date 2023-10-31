from base.base_area import BaseArea
from medicine.medicine_calculator import MedicineCalculator


class MainMenu:
    options: dict = {
        "M": "Medicine",
        "E": "Exit",
    }
    calculator_area: BaseArea | None = None

    def __init__(self) -> None:
        while True:
            self.reset_variables()
            self.show_menu()

    def reset_variables(self) -> None:
        self.calculator_area = None

    def show_options(self) -> None:
        for letter, name in self.options:
            print("\t %s - %s" % (letter, name))

    def show_menu(self) -> None:
        print("Choose the area: ")
        self.show_options()

        calculator_type: str = input()
        calculator_type = calculator_type.upper()

        self.define_area(calculator_type)

        if self.calculator_area is None:
            print("Nothing was found, please try again!")
            return

        self.instantiate_calculator_area()

    def instantiate_calculator_area(self) -> None:
        self.calculator_area.menu()
        self.calculator_area.instantiate_calculator()

    def define_area(self, calculator_type: str):
        if calculator_type == 'E':
            return

        if calculator_type == 'M':
            self.calculator_area = MedicineCalculator()


if __name__ == "__main__":
    MainMenu()
