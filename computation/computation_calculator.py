import logging
from abc import ABC

from base.base_area import BaseArea
from base.base_option import BaseOption
from computation.relu import ReLU
from computation.sigmoid import Sigmoid
from computation.tanh import TanH


class ComputationCalculator(BaseArea, ABC):
    def __init__(self):
        self.options = [
            BaseOption("ReLU", ReLU),
            BaseOption("Sigmoid", Sigmoid),
            BaseOption("TanH", TanH),
        ]
        logging.info("Calculator for computation formulas instantiated.")

