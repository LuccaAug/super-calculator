from base.base_area import BaseArea


options: dict = {
    "E": "Exit",
}


def main() -> None:
    print("Choose the area: ")
    for letter, name in options:
        print("\t %s - %s" % (letter, name))

    calculator_type = input()
    calculator_type = calculator_type.upper()

    if calculator_type == 'E':
        return

    calculator_area: BaseArea | None = None

    if calculator_area is not None:
        calculator_area.menu()
        calculator_area.instantiate_calculator()
    else:
        print("Nothing was found, please try again!")


if __name__ == "__main__":
    main()
