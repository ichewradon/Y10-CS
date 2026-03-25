#import data class decorator
from dataclasses import dataclass

#define student record
@dataclass

class Student:# this defindes the student record
    #below the information we need for the record
    first_name: str
    last_name: str
    student_id: int
    school_year: int
    working_at_grade: 0.0
    #all the above fields/ attributes - features that make up
    #the record
    #the working at grade is set to 0.0 this is a default value

#---- creating instances of students----

student1 = Student("James", "Wilkes", 12345, 10, 4.0)
student2 = Student("Bob", "Jones", 54321, 10, 3.5)
student3 = Student("Gethin", "Grice", 67676, 2, 0.6)

#----accessing the records of student 1----

print(f" student 1 name: {student1.first_name} {student1.last_name}")
print(f" student 1 ID: {student1.student_id}")
print(f" student 1 school year: {student1.school_year}")
print(f" student 1 working at grade: {student1.working_at_grade}")

#----accessing the records of student 2----

print(f" student 2 name: {student2.first_name} {student2.last_name}")
print(f" student 2 ID: {student2.student_id}")
print(f" student 2 school year: {student2.school_year}")
print(f" student 2 working at grade: {student2.working_at_grade}")

#----accessing the records of student 3----

print(f" student 3 name: {student3.first_name} {student3.last_name}")

print(f" student 3 working at grade: {student3.working_at_grade}")

#----modifying a field within a record----
student1.first_name="Johmaes"
print(f"Student name changed to: {student1.first_name}")

#----check gpa against 3.7
List1 = student1, student2, student3
for x in range(len(List1)):
    print(List1[Student].student_id)
