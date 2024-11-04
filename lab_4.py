class ArtificialTree:
    def __init__(self, manufacturer="", height=0, price=0.0, material=""):
        self.__manufacturer = manufacturer
        self.__height = height
        self.__price = price
        self.__material = material

        self.number_field = 0
        self.string_field = "Default"

    def get_manufacturer(self):
        return self.__manufacturer

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def get_material(self):
        return self.__material

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    def set_material(self, material):
        self.__material = material

    def __str__(self):
        return (f"ArtificialTree(manufacturer={self.__manufacturer}, "
                f"height={self.__height}, price={self.__price}, material={self.__material}, "
                f"number_field={self.number_field}, string_field={self.string_field})")

    def __repr__(self):
        return self.__str__()

    def __del__(self):
        print(f"ArtificialTree {self.__manufacturer} is being deleted")

def main():
    trees = [
        ArtificialTree("Ялинка Плюс", 180, 1200.5, "ПВХ"),
        ArtificialTree("Еко Ялинка", 150, 950.0, "Пластик"),
        ArtificialTree("Лісова красуня", 200, 1500.0, "Сосна")
    ]

    for tree in trees:
        print(tree)

if __name__ == "__main__":
    main()
