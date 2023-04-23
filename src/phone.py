from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return super().__repr__()[:-1] + f', {self.__number_of_sim})'

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value > 0:
            self.__number_of_sim = value

        else:
            print("Количество физических SIM-карт должно быть целым числом больше нуля.")