
class Student:
    def __init__(self, name):
        self.name: str = name
        self.attend: int = 0
        self.grades: list = []
    
    def getName(self) -> str:
        return self.name
    
    def getAttendance(self) -> int:
        return self.attend
    
    def getGrades(self) -> list:
        return self.grades
    
    def attendClass(self):
        self.attend += 1
    
    def addGrade(self, grade: str):
        self.grades.append(grade)

def main():
    student = Student("Ehsan Sumra")
    print(student.getName())

    student.attendClass()
    print(student.getAttendance())

    student.addGrade("A")
    print(student.getGrades())

main()