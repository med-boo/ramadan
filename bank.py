class Bank:
    def __init__(self, name:str):
        self.name = name
        self.money = 1000_000_000
        self.costumer = []

    def lend(self, costumer, money):
        if isinstance(costumer,Costumer):
            costumer.salaf += money
            return( f"You have been loand {money} DH.")
        else:
            return "sorry, You re not a costumer !"
    
    def returned(self, costumer, money):
        if isinstance (costumer, Costumer):
            costumer.salaf -= money
            return f"You have returned {money} DH, we still owe you {costumer.salaf} DH."
        else:
            return "sorry, You re not a costumer !"
    
class Costumer:
    def __init__(self, name,money,salaf):
        self.name = name
        self.money = money
        self.salaf = salaf

    def send_money(self, friend, money):
        self.money -= money
        friend.money += money
        return f"{self.name} has loand {friend.name} {money} DH . "
    
# assert 1+1 == 5, "they not equal"

attijary = Bank("attijaryWafaBank")
# print(attijary.money)
# print(attijary.costumer)
# assert attijary.money == 1000_000_000

nabil = Costumer("nabil", 10, 0)
# print(attijary.lend(nabil, 20))
# print(nabil.salaf)
# print(attijary.returned(nabil, 5))
khalid = Costumer("Khalid", 1000, 0)

# print(nabil.money)
print(khalid.money)
print(nabil.send_money(khalid, 200))
print(khalid.money)
print(nabil.money)