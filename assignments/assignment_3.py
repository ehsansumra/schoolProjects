
class VeganHamburger:

    def __init__(self, weight: int, doneness: str, cheese: bool, toppings: list):
        self.weight = weight
        self.doneness = doneness
        self.cheese = cheese
        self.toppings = toppings
    
    def __str__(self):
        return (
            f'Weight: {self.weight} \nDoneness: {self.doneness}' +
            f'\nCheese: {self.cheese} \nToppings: {self.toppings}'
               )

    def getWeight(self) -> int:
        return self.weight
    
    def setWeight(self, weight: int) :
        self.weight = weight
 
    def getDoneness(self) -> str:
        return self.doneness
    
    def setDoneness(self, string: str):
        self.doneness = string

    def getCheese(self) -> bool:
        return self.cheese
    
    def toggleCheese(self):
        if self.cheese:
            self.cheese = False
        else:
            self.cheese = True

    def getToppings(self) -> list:
        return self.toppings
    
    def setToppings(self, toppings: list):
        self.toppings = toppings
    
    def bite(self):
        if self.weight > 0:
            self.weight -= 1

def enterToppings() -> list:
    toppings = []

    while True:
        topping = input("Enter a topping. (Enter nothing to end) ")
        if topping:
            toppings.append(topping)
        else:
            return toppings

def parseCheese(option) -> bool:
    option = option.replace(" ", "")
    option = option.upper()

    if option == "YES":
        return True
    elif option == "NO":
        return False
    else:
        return False

def inputBurger() -> VeganHamburger:
    print(" --- New Burger --- ")
    weight: int = int(input("How many ounces of burger would you like? "))
    doneness: str = input("How well would you like it done? ")
    cheese: bool = parseCheese(input("Cheese or no cheese? (Yes or No) "))
    toppings: list = enterToppings()

    veganHamburger = VeganHamburger(weight, doneness, cheese, toppings)
    return veganHamburger

def weightGetter(e):
    return e.getWeight()

def tester():
    b = [VeganHamburger(4, "well", True, []), VeganHamburger(1, "well", True, []), VeganHamburger(8, "well", True, [])]
    printWeight(b)
    sorted = sortByWeight(b)
    printWeight(sorted)
    print(sorted[1].__str__())


def printWeight(bList):
    for b in bList:
        print(b.weight)

def sortByWeight(burgerList) -> list:
    burgerList.sort(key=weightGetter)
    return burgerList

def main() -> list:
    print("Order three vegan hamburgers.")
    burgerList = []
    for i in range(3):
        burger = inputBurger()
        burgerList.append(burger)
    printWeight(burgerList)
    sortBurgers = sortByWeight(burgerList)
    printWeight(sortBurgers)
    
# TODO more work to be done
tester()