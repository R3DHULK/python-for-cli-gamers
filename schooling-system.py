class School:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
    
    def status(self):
        print(f"{self.name} has {len(self.students)} students.")
    
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.absences = 0
        self.gpa = 4.0
    
    def attend_class(self):
        self.absences += 1
        if self.absences > 5:
            self.gpa -= 0.5
    
    def study(self):
        self.gpa += 0.1
    
    def status(self):
        print(f"{self.name} is in grade {self.grade}, has a {self.gpa} GPA, and has {self.absences} absences.")

def main():
    school = School("ABC School")
    
    while True:
        school.status()
        action = input("What would you like to do? (add student, remove student, attend class, study, exit) ")
        
        if action == "add student":
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            student = Student(name, grade)
            school.add_student(student)
        elif action == "remove student":
            name = input("Enter student name: ")
            for student in school.students:
                if student.name == name:
                    school.remove_student(student)
                    break
        elif action == "attend class":
            name = input("Enter student name: ")
            for student in school.students:
                if student.name == name:
                    student.attend_class()
                    break
        elif action == "study":
            name = input("Enter student name: ")
            for student in school.students:
                if student.name == name:
                    student.study()
                    break
        elif action == "exit":
            break
        else:
            print("Invalid action. Please try again.")
    
    print("Thanks for playing!")

if __name__ == '__main__':
    main()
