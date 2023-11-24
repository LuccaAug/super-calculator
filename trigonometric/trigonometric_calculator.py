import logging
from abc import ABC

from base.base_area import BaseArea
from base.base_option import BaseOption
from trigonometric.cosecant import Cosecant
from trigonometric.cosine import Cosine
from trigonometric.cotangent import Cotangent
from trigonometric.secant import Secant
from trigonometric.sine import Sine
from trigonometric.tangent import Tangent


class TrigonometricCalculator(BaseArea, ABC):
    def __init__(self):
        self.options = [
            BaseOption("Cosecant", Cosecant()),
            BaseOption("Cosine", Cosine()),
            BaseOption("Cotangent", Cotangent()),
            BaseOption("Secant", Secant()),
            BaseOption("Sine", Sine()),
            BaseOption("Tangent", Tangent()),
        ]
        logging.info("Calculator for trigonometric formulas instantiated.")

