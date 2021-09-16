
class Student:
    def __init__(self, name: str, attend: int = 0):
        self.name: str = name
        self.attend: int = attend
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
    student.addGrade("A+")
    student.addGrade("A-")
    print(student.getGrades())

if __name__ == "__main__":
    main()