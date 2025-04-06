class Weapons ():
    def __init__(self, durability, made_of):
        self.durability = durability
        self.madeof = made_of
    

class Plants ():
    def __init__(self):
        pass

axe = Weapons(100, "wood")
apple = Plants()
print(axe)
print(axe.durability)
print(axe.madeof)
print(apple)

class Dagger(Weapons):
    def __init__(self, durability, made_of, shape, color = "wooden", is_enchanted = False):
        super().__init__(durability, made_of)
        self.shape = shape
        self.color = color
        self.isenchanted = is_enchanted
    def cut_things(self, thing):
        pass

class Axe(Weapons):
    def __init__(self, durability, made_of,shape, color = "silver", is_enchanted = False):
        super().__init__(durability, made_of)
        self.shape = shape
        self.color = color
        self.isenchanted = is_enchanted
    def cut_things(self, thing):
        pass

class Sword(Weapons):
     def __init__(self, durability, made_of,shape, color = "silver", is_enchanted = False):
        super().__init__(durability, made_of)
        self.shape = shape
        self.color = color
        self.isenchanted = is_enchanted
     def cut_things(self, thing):
        pass

class Pinetree(Plants):
    def __init__(self, color, length, texture = "TREE" ):
        super().__init__()
        self.color = color
        self.length = length
        self.texture = texture
    def gives(self,):
        pass

class Starwberry(Plants):
    def __init__(self, color, length, texture = "ARBORESCENTE" ):
        super().__init__()
        self.color = color
        self.length = length
        self.texture = texture
    def gives(self,):
        pass
        
class Sugar_can(Plants):
    def __init__(self, color, length, texture = "PERENNIAL" ):
        super().__init__()
        self.color = color
        self.length = length
        self.texture = texture
    def gives(self,):
        pass