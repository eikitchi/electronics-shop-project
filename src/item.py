import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise ValueError("Наименование товара не может быть больше 10 символов")
        self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует все товара из файла csv.
        """
        try:
            with open(os.path.join(os.path.dirname(__file__), "items.csv"), 'r') as f:
                reader = csv.DictReader(f)
                cls.all = []
                for i in reader:
                    try:
                        if len(i) != 3 or i.get('name') is None or i.get('price') is None or i.get('quantity') is None:
                            raise InstantiateCSVError
                    except InstantiateCSVError as err:
                        print(err.message)
                        break
                    else:
                        cls(i['name'], i['price'], i['quantity'])

        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(string):
        return int(float(string)) if '.' in string else int(string)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
