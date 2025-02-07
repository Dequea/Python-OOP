from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, model: str, speed_limit: int) -> None:
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken: bool = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    @abstractmethod
    def speed_limit(self):
        pass

    @speed_limit.setter
    @abstractmethod
    def speed_limit(self, value):
        pass

    @property
    @abstractmethod
    def car_type(self):
        pass
