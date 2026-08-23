print("\n----- Student Marks Calculator -----")

name = input("\nEnter your name: ")
marks1 = float(input("Enter your Subject1 Marks: "))
marks2 = float(input("Enter your Subject2 Marks: "))
marks3 = float(input("Enter your Subject3 Marks: "))
marks4 = float(input("Enter your Subject4 Marks: "))
marks5 = float(input("Enter your Subject5 Marks: "))

print("\nStudent name:", name)
print("\nSubject1:", marks1)
print("Subject2:", marks2)
print("Subject3:", marks3)
print("Subject4:", marks4)
print("Subject5:", marks5)

print("\nTotal marks:",(marks1 + marks2 + marks3 + marks4 + marks5))
print("Average marks:",((marks1 + marks2 + marks3 + marks4 + marks5)/5))