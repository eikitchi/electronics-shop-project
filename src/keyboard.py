from src.item import Item


class Mixinlanguage:
    language = "EN"

    def __init__(self, *args):
        super().__init__(*args)

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        return self


class KeyBoard(Item, Mixinlanguage):
    def __init__(self, *args):
        super().__init__(*args)
