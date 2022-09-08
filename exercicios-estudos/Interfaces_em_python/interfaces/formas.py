from abc import ABC, abstractmethod


class formasInterface(ABC):
    @abstractmethod
    def get_perimetro(self):
        pass
    @abstractmethod
    def get_area(self):
        pass
