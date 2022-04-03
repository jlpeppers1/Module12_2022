from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def sides(self):
        raise NotImplementedError("Abstract method not implemented")
