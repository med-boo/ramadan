def sum_squares(start,length):
    squares = 0
    for i in range(start, start+length):
        squares += i*i
    return squares
# print(sum_squares(1,3))

class Person():
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Teacher(Person):
    def __init__(self,name,color, religion, nationality):
        super().__init__(name,color)
        self.religion = religion
        self.nationality = nationality
        self.salary = 10000
    def slaps_student(self,name):
        return (f"{self.name} has slaped {name} twice in his face.")
    
ahmed = Teacher("achraf", "Black","Muslim","Morrocan")
print(ahmed.slaps_student("jalal"))


class Modir(Person):
    def __init__(self, name, color, height, glasses):
        super().__init__(name, color)
        self.height = height
        self.glasses = glasses
    def get_rid(self,brwita):
        return f"{self.name} has gotten rid of {brwita.name}"
jhbdv = Modir("Khalid", "Red", 1.81, "on")
print(jhbdv.get_rid(ahmed))

