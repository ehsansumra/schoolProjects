
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

# bite 50 times.
def bite50(burger: VeganHamburger):
    for i in range(50):
        burger.bite()
# A quick tester that doesn't require user input
# Call instead of main to see the output
def tester():
    burgers = [VeganHamburger(4, "well", True, ["lettuce", "mayo"]), VeganHamburger(1, "well", True, ["onions", "tomato"]), VeganHamburger(8, "well", True, ["pickles", "ketchup"])]
    printBurger(burgers, "\n--- Unsorted Burgers ---")
    sortedBurgers = sortByWeight(burgers)
    printBurger(sortedBurgers, "\n--- Sorted Burgers ---")
    testGetterSetter(sortedBurgers[0])

def testGetterSetter(burger: VeganHamburger):
    print("\n--- Testing Getters Setters ---")
    
    print("\nWeight: ", burger.getWeight())
    burger.setWeight(30)
    print("Set Weight: ", burger.getWeight())
    bite50(burger)
    print("Bite 50 times weight: ", burger.getWeight())
    
    print("\nCheese: ", burger.getCheese())
    burger.toggleCheese()
    print("Set Cheese: ", burger.getCheese())

    print("\nDoneness: ", burger.getDoneness())
    burger.setDoneness("testDoneness")
    print("Set Doneness: ", burger.getDoneness())

    print("\nToppings: ", burger.getToppings())
    burger.setToppings(['test'])
    print("Set Toppings: ", burger.getToppings())

def printBurger(bList, msg =""):
    print(msg)
    for b in bList:
        print(b.__str__())
        print("-------")

def weightGetter(burger: VeganHamburger):
    return burger.getWeight()

# .sort method using weightGetter() as a key
def sortByWeight(burgerList) -> list:
    burgerList.sort(key=weightGetter)
    return burgerList

def inputBurger() -> VeganHamburger:
    print(" --- New Burger --- ")
    weight: int = int(input("How many ounces of burger would you like? "))
    doneness: str = input("How well would you like it done? ")
    cheese: bool = parseCheese(input("Cheese or no cheese? (Yes or No) "))
    toppings: list = enterToppings()

    return VeganHamburger(weight, doneness, cheese, toppings)

# prompt user to input 3 burgers, sort them by weight and display
# also test getters and setters on one burger.
def main() -> list:
    print("Order three vegan hamburgers.")
    burgerList = []
    for i in range(3):
        burger = inputBurger()
        burgerList.append(burger)
    printBurger(burgerList, "\n--- Unsorted Burgers ---")

    sortBurgers = sortByWeight(burgerList)
    printBurger(sortBurgers, "\n--- Sorted By Weight ---")
    testGetterSetter(sortBurgers[1])
    

if __name__ == "__main__":
    main()
    # comment out main to use tester()
    # tester() 
