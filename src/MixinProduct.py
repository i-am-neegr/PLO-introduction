class MixinProduct:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, *args):
        if self.quantity < 1:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        print(self.__repr__())

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
