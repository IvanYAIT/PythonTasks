class Child:
    is_hungry = True
    is_calm = False

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def feed(self):
        if self.is_hungry:
            self.is_hungry = False
            print(f'{self.name} поел')
        else:
            print(f'{self.name} не голоден')
    
    def calm(self):
        if not self.is_calm:
            self.is_calm = True
            print(f'{self.name} успокоился')
        else:
            print(f'{self.name} спокоин')

class Parent:
    def __init__(self, name, age, *childrens):
        self.name = name
        self.age = age
        self.childrens = childrens
    
    def get_info(self):
        print(f"Меня зовут {self.name}, мне {self.age}")
    
    def feed_childrens(self):
        for child in self.childrens:
            child.feed()
    
    def calm_childrens(self):
        for child in self.childrens:
            child.calm()