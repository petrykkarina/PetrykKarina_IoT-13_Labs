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

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material

    
    def __str__(self):
        return f"ArtificialTree(manufacturer={self.__manufacturer}, height={self.__height}, price={self.__price}, material={self.__material})"

    def __repr__(self):
        return self.__str__()

    
    def __del__(self):
        print(f"ArtificialTree {self.__manufacturer} is being deleted")


if __name__ == "__main__":
    tree1 = ArtificialTree("TreeCorp", 150, 59.99, "Plastic")
    tree2 = ArtificialTree("EverGreen", 180, 89.99, "PVC")
    tree3 = ArtificialTree("EcoTrees", 200, 120.50, "Recycled Plastic")

   
    print(tree1)
    print(tree2)
    print(tree3)
