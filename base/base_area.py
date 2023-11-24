from abc import abstractmethod

from base.base_calculator import BaseCalculator
from base.base_option import BaseOption


class BaseArea:
    options: list[BaseOption]
    chose_calculator: BaseCalculator

    @abstractmethod
    def menu(self) -> None:
        print("Choose the formula: ")
        for index, option in enumerate(self.options):
            print("\t %2i - %s" % (index + 1, option.name))

        chose_str = input()
        chose_index = int(chose_str) - 1
        chose_option = self.options[chose_index]
        self.chose_calculator = chose_option.calculator

    def instantiate_calculator(self) -> None:
        self.chose_calculator.ask_requirements()
        result = self.chose_calculator.do_math()
        print(result)
        print()
