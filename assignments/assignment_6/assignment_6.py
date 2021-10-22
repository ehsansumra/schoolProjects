from Employee import Employee
from Queue import Queue

# Reads the dirany.txt file and returns an array of strings contain the data from each line.
def readTxt():
    data = open('dirany.txt', 'r')
    txt = data.readlines()
    data.close()
    return txt

# Each line has one employee on it
# data.readlines() returns a list that has a string for each element.
# The string has the first name, last name, and employee pay separated by spaces
# Each string is turned into a list with the split() function, and each element of the list is indexed accordingly
# Each of these values are then passed to initialize and return a new Employee object.
def parseEmployee(employeeStr: str):
    empList = employeeStr.split()
    # assigned them to variables to make it readable
    first = empList[0]
    last = empList[1]
    pay = int(empList[2])
    return Employee(first, last, pay)

# This function parses the array returned by data.readlines()
# Uses the parseEmployee helper function to create an Employee object for each line in the txt.
# Each employee is enqueued in the order they were read from the file.
def parseEmployees(txt: str):
    empQueue = Queue()
    for employeeStr in txt:
        employee = parseEmployee(employeeStr)
        empQueue.enqueue(employee)

    return empQueue

# Takes the queue created by parseEmployees
# Dequeue the employee, set their bonus, decrement bonus by 0.01
# Total bonus is calculated at the same time.
# Employees are put back into the queue
def setBonus(empQ: Queue):
    bonus = 0.20
    bonusTotal = 0
    length = empQ.size()

    for i in range(length):
        employee = empQ.dequeue()
        employee.setBonus(bonus)
        bonusTotal += employee.getBonus()

        empQ.enqueue(employee)
        bonus -= 0.01
    
    return bonusTotal

# Function that prints the fields of each employee object in a clean manner
# Returns the queue to its original state
def cleanPrint(empQ: Queue):
    length = empQ.size()
    for i in range(length):
        employee = empQ.dequeue()
        print(employee)
        empQ.enqueue(employee)

# The file is read by readTxt()
# An employee object is created based off of the data in each line
# Each employee is entered into the queue in the order they were read
# The count of employees is calculated by calling empQueue.size()
# The bonus is calculated for each employee, as well as the total bonus for all employees
# The queue is returned to its original order
def main():
    txt = readTxt()
    empQueue = parseEmployees(txt)
    cleanPrint(empQueue)
    print("\nNumber of Employees: ", empQueue.size())

    empCount = empQueue.size()
    bonusTotal = setBonus(empQueue)
    print("Employee Count", empCount)
    print("Total Bonus", bonusTotal)
    print("\n---- AFTER BONUS ----\n")
    cleanPrint(empQueue)

if __name__ == "__main__":
    main()