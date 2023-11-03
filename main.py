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


def show_menu() -> None:
    print("Choose the area: ")
    for letter, name in options:
        print("\t %s - %s" % (letter, name))


def instantiate_calculator_area(calculator_area: BaseArea) -> None:
    calculator_area.menu()
    calculator_area.instantiate_calculator()


def main():
    in_loop: bool = True
    while in_loop:
        calculator_area: BaseArea | None = None

        show_menu()

        calculator_type: str = input()
        calculator_type = calculator_type.upper()

        if calculator_type == 'E':
            in_loop = False

        elif calculator_type == 'M':
            calculator_area = MedicineCalculator()

        elif calculator_type == 'C':
            calculator_area = ComputationCalculator()

        elif calculator_type == 'P':
            calculator_area = PhysicCalculator()

        elif calculator_type == 'T':
            calculator_area = TrigonometricCalculator()

        if calculator_area is None:
            print("Nothing was found, please try again!")
            continue

        instantiate_calculator_area(calculator_area)

    print("Thanks for using the super-calculator! :D")


if __name__ == "__main__":
    main()
