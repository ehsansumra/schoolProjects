
class SocialEvent:

    def __init__(self, title: str, date: str, attendees: int):

        self.title = title
        self.date = date
        self.attendees = attendees

    def __str__(self):
        return f'Title: {self.title}, Date: {self.date}, Attendees: {self.attendees}'

    def getTitle(self):
        return self.title
    
    def getDate(self):
        return self.date

    def getAttendees(self):
        return self.attendees
    
    def setTitle(self, title: str):
        self.title = title
    
    def setDate(self, date: str):
        self.date = date
    
    def setAttendees(self, attendees: str):
        self.attendees = attendees

# Used as .sort key
def attendeeGetter(event: SocialEvent):
    return event.getAttendees()

# Input prompts for each event parameter
def inputEvent():
    title = input("Event Name: ")
    date = input("Event date: ")
    attendees = int(input("Number of attendees: "))

    return (SocialEvent(title, date, attendees))

# sorting a list of SocialEvents by the number of attendees
def sortByAttendees(eventList: list):
    eventList.sort(key = attendeeGetter, reverse = True)
    return eventList

# printing each SocialEvent in the list using .__str__()
def printEventList(eventList: list, msg = ""):
    print(msg)
    for event in eventList:
        print(event.__str__())

# Test function
def testSorting():
    b = [SocialEvent("Birthday Party", "10/15/21", 9), SocialEvent("Graduation", "6/5/23", 90), SocialEvent("Barbecue", "7/26/22", 20)]
    printEventList(b, "\n--- Unsorted Events ---")
    sortedEventList = sortByAttendees(b)
    printEventList(sortedEventList, "\n--- Sorted By Attendees ---")
    testGettersSetters(sortedEventList[0])

# Testing getters and setters
def testGettersSetters(event: SocialEvent):
    print("\n--- Getter Setter Test ---")
    print("Title:", event.getTitle())
    event.setTitle("testTitle")
    print("Set Title:", event.getTitle())

    print("Date:", event.getDate())
    event.setDate("test/test/test")
    print("Set Date:", event.getDate())

    print("Attendees:", event.getAttendees())
    event.setAttendees(500)
    print("Set Attendees:", event.getAttendees())

""" Prompt user to input 3 SocialEvents
    Print out the SocialEvents sorted by number of attendees"""
def main():
    eventList = []
    for i in range(3):
        event = inputEvent()
        eventList.append(event)

    printEventList(eventList, "\n--- Unsorted Events ---")

    sortedEventList = sortByAttendees(eventList)
    printEventList(sortedEventList, "\n--- Sorted By Attendees ---")
    testGettersSetters(sortedEventList[0])

testSorting()