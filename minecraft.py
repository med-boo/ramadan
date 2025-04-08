class Weapons ():
    def __init__(self, durability, made_of):
        self.durability = durability
        self.madeof = made_of
    

class Plants ():
    def __init__(self):
        pass


class Dagger(Weapons):
    def __init__(self, durability, made_of, shape, color = "wooden", is_enchanted = False):
        super().__init__(durability, made_of)
        self.shape = shape
        self.color = color
        self.isenchanted = is_enchanted
    def cut_things(self, thing):
        if isinstance(thing, Plants):
            if self.durability > 0:
                if thing.texture == "ARBORESCENTE":
                    print(thing.gives(self.isenchanted))
                    self.durability -= 20
                    return "you have cut the plant and the durability of your weapon has decreased."
                else:
                    return("Your weapon Can't cut this plant.")
            else:
                return("The durability of your weapon is less than 0")
         
        else:
            return("You can't break a non-plant thing with your weapon")
        
                

class Axe(Weapons):
    def __init__(self, durability, made_of,shape, color = "silver", is_enchanted = False):
        super().__init__(durability, made_of)
        self.shape = shape
        self.color = color
        self.isenchanted = is_enchanted
    def cut_things(self, thing):
        if isinstance(thing, Plants):
            if self.durability > 0:
                if thing.texture == "ARBORESCENTE" or thing.texture == "TREE":
                    print(thing.gives(self.isenchanted))
                    self.durability -= 5

                    return "you have cut the plant and the durability of your weapon has decreased."
                else:
                    return("Your weapon Can't cut this plant.")
            else:
                return("The durability of your weapon is less than 0")
         
        else:
            return("You can't break a non-plant thing with your weapon")

class Sword(Weapons):
     def __init__(self, durability, made_of,shape, color = "silver", is_enchanted = False):
        super().__init__(durability, made_of)
        self.shape = shape
        self.color = color
        self.isenchanted = is_enchanted
     def cut_things(self, thing):
        if isinstance(thing, Plants):
            if self.durability > 0:
                if thing.texture == "ARBORESCENTE" or thing.texture == "TREE" or thing.texture == "PERENNIAL":
                    print(thing.gives(self.isenchanted))
                    self.durability -= 10
                    return "you have cut the plant and the durability of your weapon has decreased."
                else:
                    return("Your weapon Can't cut this plant.")
            else:
                return("The durability of your weapon is less than 0")
         
        else:
            return("You can't break a non-plant thing with your weapon")

class Pinetree(Plants):
    def __init__(self, color, length, texture = "TREE" ):
        super().__init__()
        self.color = color
        self.length = length
        self.texture = texture
    def gives(self, enchanted):
        if enchanted:
            return("You got 2 fruits.")
        else:
            return("You got 1 fruits.")
        

        

class Strawberry(Plants):
    def __init__(self, color, length, texture = "ARBORESCENTE" ):
        super().__init__()
        self.color = color
        self.length = length
        self.texture = texture
    def gives(self,enchanted):
        if enchanted:
            return("You got 2 fruits.")
        else:
            return("You got 1 fruits.")
        
class Sugar_can(Plants):
    def __init__(self, color, length, texture = "PERENNIAL" ):
        super().__init__()
        self.color = color
        self.length = length
        self.texture = texture
    def gives(self,enchanted):
        if enchanted:
            return("You got 2 fruits.")
        else:
            return("You got 1 fruit.")

axe = Axe(50, "stone", "round", is_enchanted= True)
straw = Strawberry("red", "big")
arsalan = Dagger(60, "Iron", "Aigu", "silver", True)
chajara = Pinetree("brown", 3)
for i in range(11):
    if arsalan.durability == 0:
        break
    
    print(arsalan.cut_things(straw))
    print(arsalan.durability)

#print(straw.gives(True))