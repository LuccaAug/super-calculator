from abc import ABC, abstractmethod


class BaseCalculator(ABC):
    @abstractmethod
    def ask_requirements(self) -> None:
        pass

    @abstractmethod
    def do_math(self) -> float:
        pass
