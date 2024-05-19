from department import Department
from student import Student
from module import Module
from lecturer import Lecturer


stu1 = Student("Devi", 200134564500)
stu2 = Student("Dasu", 199867540987)
stu3 = Student("Dinusha", 200345379871)

module1 = Module("Maths", "IM3245")
module2 = Module("Programming", "DA3256")
module3 = Module("Operation Management, "BA4532")

dep1 = Department("Civil")
dep2 = Department("IT")

lec1 = Lecturer("Perera", 200123)
lec2 = Lecturer("Gunawardhana", 200124)

age = 12
print("Hi, New Student")
print(age)
print(stu2.nic)
print(module1.name)
print(dep1.name)
print(lec1.id)

