import logging
from abc import ABC

from base.base_area import BaseArea
from base.base_option import BaseOption
from physic.work import Work
from physic.speed import Speed
from physic.kinetic import Kinetic
from physic.potential import Potential
from physic.gravitation import Gravitation
from physic.acceleration import Acceleration


class PhysicCalculator(BaseArea, ABC):
    def __init__(self):
        self.options = [
            BaseOption("Work", Work()),
            BaseOption("Speed", Speed()),
            BaseOption("Kinetic", Kinetic()),
            BaseOption("Potential", Potential()),
            BaseOption("Gravitation", Gravitation()),
            BaseOption("Acceleration", Acceleration()),
        ]
        logging.info("Calculator for physics formulas instantiated.")

