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


def main():
    in_loop: bool = True
    while in_loop:
        calculator_area: BaseArea | None = None

        print("Choose the area: ")
        for letter, name in options:
            print("\t %s - %s" % (letter, name))

        calculator_type: str = input()
        calculator_type = calculator_type.upper()

        if calculator_type == 'E':
            in_loop = False

        else:
            if calculator_type == 'M':
                calculator_area = MedicineCalculator()

            else:
                if calculator_type == 'C':
                    calculator_area = ComputationCalculator()

                else:
                    if calculator_type == 'P':
                        calculator_area = PhysicCalculator()

                    else:
                        if calculator_type == 'T':
                            calculator_area = TrigonometricCalculator()

                        else:
                            if calculator_area is None:
                                print("Nothing was found, please try again!")
                                continue

        calculator_area.menu()
        calculator_area.instantiate_calculator()

    print("Thanks for using the super-calculator! :D")


if __name__ == "__main__":
    main()
