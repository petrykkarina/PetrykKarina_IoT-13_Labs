class ArtificialTree:
    def __init__(self, manufacturer='', height=0, price=0.0, material='', public_num_field=0, public_str_field=''):
       
        self.__manufacturer = manufacturer
        self.__height = height
        self.__price = price
        self.__material = material

        
        self.public_num_field = public_num_field  
        self.public_str_field = public_str_field  

    
    def __init__(self):
        self.__manufacturer = "Невідомий"
        self.__height = 0
        self.__price = 0.0
        self.__material = "Невідомий"
        self.public_num_field = 0
        self.public_str_field = "Невідомий"

    
    def __init__(self, manufacturer='', height=0, price=0.0, material='', public_num_field=0, public_str_field=''):
        self.__manufacturer = manufacturer
        self.__height = height
        self.__price = price
        self.__material = material
        self.public_num_field = public_num_field  
        self.public_str_field = public_str_field  

    
    def __del__(self):
        print(f'Об\'єкт {self.__manufacturer} видалено')

    
    def get_manufacturer(self):
        return self.__manufacturer

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def get_material(self):
        return self.__material

    
    def __str__(self):
        return f'Штучна ялинка: {self.__manufacturer}, Висота: {self.__height} см, Ціна: {self.__price} грн, Матеріал: {self.__material}'

    def __repr__(self):
        return f'ArtificialTree(manufacturer={self.__manufacturer}, height={self.__height}, price={self.__price}, material={self.__material})'



if __name__ == "__main__":
   
    tree1 = ArtificialTree("Ялинка Плюс", 180, 1200.5, "ПВХ", 5, "Декор")
    tree2 = ArtificialTree("Еко Ялинка", 150, 950.0, "Пластик", 3, "Зелений")
    tree3 = ArtificialTree("Лісова красуня", 200, 1500.0, "Сосна", 8, "Природний")

    
    for tree in (tree1, tree2, tree3):
        print(tree)
