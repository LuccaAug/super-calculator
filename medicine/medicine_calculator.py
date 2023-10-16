import logging
from abc import ABC

from base.base_area import BaseArea
from base.base_option import BaseOption
from medicine.bmi import BMI
from medicine.bmr import BMR


class MedicineCalculator(BaseArea, ABC):
    def __init__(self):
        self.options = [
            BaseOption("BMI", BMI),
            BaseOption("BMR", BMR),
        ]
        logging.info("Calculator for medicine formulas instantiated.")

