class Weapons ():
    def __init__(self, durability, made_of, breakable = True ):
        self.durability = durability
        self.madeof = made_of
        self.breakable = breakable

class Plants ():
    def __init__(self):
        pass


class Dagger(Weapons):
    def __init__(self, durability, made_of, breakable, shape, color = "wooden", is_enchanted = False):
        super().__init__(durability, made_of,breakable)
        self.shape = shape
        self.color = color
        self.isenchanted = is_enchanted
    def cut_things(self, thing):
        if isinstance(thing, Plants):
            if self.durability > 0:
                if thing.texture == "ARBORESCENTE":
                    print(thing.gives(self.isenchanted))
                    if self.breakable:
                        self.durability -= 20
                    
                    return "you have cut the plant and the durability of your weapon has decreased."
                else:
                    return("Your weapon Can't cut this plant.")
            else:
                return("The durability of your weapon is less than 0")
         
        else:
            return("You can't break a non-plant thing with your weapon")
        
                

class Axe(Weapons):
    def __init__(self, durability, breakable, made_of,shape, color = "silver", is_enchanted = False):
        super().__init__(durability, made_of,breakable)
        self.shape = shape
        self.color = color
        self.isenchanted = is_enchanted
    def cut_things(self, thing):
        if isinstance(thing, Plants):
            if self.durability > 0:
                if thing.texture == "ARBORESCENTE" or thing.texture == "TREE":
                    print(thing.gives(self.isenchanted))
                    if self.breakable:

                        self.durability -= 5

                    return "you have cut the plant and the durability of your weapon has decreased."
                else:
                    return("Your weapon Can't cut this plant.")
            else:
                return("The durability of your weapon is less than 0")
         
        else:
            return("You can't break a non-plant thing with your weapon")

class Sword(Weapons):
     def __init__(self, durability,made_of, shape, sharpeness,breakable, color = "silver", is_enchanted = False, ):
        super().__init__(durability, made_of,breakable)
        self.shape = shape
        self.sharpness = sharpeness
        self.color = color
        self.isenchanted = is_enchanted
     def cut_things(self, thing):
        if isinstance(thing, Plants):
            if self.durability > 0:
                if thing.texture == "ARBORESCENTE" or thing.texture == "TREE" or thing.texture == "PERENNIAL":
                    print(thing.gives(self.isenchanted))
                    if self.breakable:
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

# axe = Axe(50, "stone", "round", is_enchanted= True)
# straw = Strawberry("red", "big")
# arsalan = Dagger(60, "Iron", "Aigue", "silver", True)
# chajara = Pinetree("brown", 3)


# if arsalan.durability == 0:    
#     print(arsalan.cut_things(straw))
#     print(arsalan.durability)

#print(straw.gives(True))
# TODO enchant the weapons to encrease there durability.
class Magic_books():
    def __init__(self, magic_type):
        self.magicstype = magic_type
    def enchant(self, sla7):
        pass

class Unbreaking(Magic_books):
    def __init__(self, level, magic_type = "power"):
        super().__init__(magic_type)
        self. level = level

    def enchant(self, sla7):
        if isinstance(sla7, Weapons):
            sla7.durability += 10 * self.level
            return (f"Your weapon has been enchanted with unbreaking {self.level} .")
        else:
            return "These books can only be applied to weapons!"

# book = Unbreaking(2)
# print(arsalan.durability)
# print(book.enchant(arsalan))
# print(arsalan.durability)

class Sharpeness(Magic_books):
    def __init__(self, level, magic_type = "sharp"):
        super().__init__(magic_type)
        self. level = level
    def enchant(self, sla7):
        if isinstance(sla7, Sword):
            sla7.sharpness += 20 * self.level
            return (f"You have applied sharpness{self.level} to your sword.")
        else:
            return "This book can only be applied to a sword."

# book = Sharpeness(1)
sayf = Sword(100, "diamond", "long", 100,True, "silver", is_enchanted= True)
# print(sayf.sharpness)
# print(book.enchant(sayf))
# print(sayf.sharpness)

# print(sayf.durability)
# sayf.durability += 30
# print(sayf.durability)
# print(sayf.color)
# sayf.color = "red"
# print(sayf.color)


class Hard(Magic_books):
    def __init__(self, magic_type = "Hardness"):
        super().__init__(magic_type)
    
    def enchant(self, sla7):
        if isinstance(sla7, Weapons):
            sla7.breakable = False
            return "Your weapon will no longer break"
        else:
            return "This book can only be applied to weapons"
        
book = Hard()
chjra = "aziz"
print(sayf.breakable)
print(book.enchant(sayf))
print(sayf.breakable)

        
            
        


         

        