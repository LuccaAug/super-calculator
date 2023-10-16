from base.base_calculator import BaseCalculator


class BMR(BaseCalculator):
    weight: float
    height: float
    age: int

    k: float
    k_weight: float
    k_height: float
    k_age: float

    def set_constants_for_man(self) -> None:
        self.k = 88.362
        self.k_weight = 13.397
        self.k_height = 4.799
        self.k_age = 5.677

    def set_constants_for_woman(self) -> None:
        self.k = 447.593
        self.k_weight = 9.247
        self.k_height = 3.098
        self.k_age = 4.330

    def ask_requirements(self) -> None:
        while True:
            sex = input("Sex (M/W): ")
            if sex.upper() == 'M':
                self.set_constants_for_man()
                break
            if sex.upper() == 'W':
                self.set_constants_for_woman()
                break
            else:
                print("Please, type only M for man or W for Woman.")

        age_str = input("Age (years): ")
        self.age = int(age_str)

        height_str = input("Height (centimeters): ")
        self.height = float(height_str)

        weight_str = input("Weight (kilograms): ")
        self.weight = float(weight_str)

    def do_math(self) -> float:
        part_1 = self.k_weight * self.weight
        part_2 = self.k_height * self.height
        part_3 = self.k_age * self.age

        bmr = self.k + part_1 + part_2 - part_3

        return round(bmr, 2)
