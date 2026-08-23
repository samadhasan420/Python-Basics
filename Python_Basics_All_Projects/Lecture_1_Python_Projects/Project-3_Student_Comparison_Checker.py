print("\n----- Student Comparison Checker -----")

student1 = input("Student 1 name: ")
marks1 = float(input("Student 1 marks: "))

student2 = input("Student 2 name: ")
marks2 = float(input("Student 2 marks: "))

print("\nstudent 1 name:",student1)
print("student 1 marks:",marks1)

print("\nstudent 2 name:",student2)
print("student 2 marks:",marks2)

equal = marks1 == marks2
not_equal = marks1 != marks2
greater = marks1 > marks2
greater_equal = marks1 >= marks2
less_than = marks1 < marks2
less_than_equal = marks1 <= marks2

print("\nStudent 1 marks == Student 2 marks: ",equal)
print("Student 1 marks != Student 2 marks: ",not_equal)
print("Student 1 marks > Student 2 marks: ",greater)
print("Student 1 marks >= Student 2 marks: ",greater_equal)
print("Student 1 marks < Student 2 marks: ",less_than)
print("Student 1 marks <= Student 2 marks: ",less_than_equal)