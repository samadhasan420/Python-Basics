print("----- Student Report Card -----")

Student_Name = str(input("\nStudent Name: "))
Science_Marks = float(input("Scienc Marks: "))
Math_Marks = float(input("Mathematics Marks: "))
English_Marks = float(input("English Marks: "))
Sst_Marks = float(input("Social Studies Marks: "))
Urdu_Sans_marks = float(input("Urdu/Sanskrit Marks: "))

Total_Marks = Science_Marks + Math_Marks + English_Marks + Sst_Marks + Urdu_Sans_marks
Percentage = (Total_Marks / 500) * 100

if Science_Marks >= 90:
    Science_Grade = "A"
elif Science_Marks >= 80:
    Science_Grade = "B"
elif Science_Marks >= 70:
    Science_Grade = "C"
elif Science_Marks >= 60:
    Science_Grade = "D"
elif Science_Marks >= 50:
    Science_Grade = "E"
elif Science_Marks >= 40:
    Science_Grade = "F"
else:
    Science_Grade  = "Fail"

if Math_Marks >= 90:
    Math_Grade = "A"
elif Math_Marks >= 80:
    Math_Grade = "B"
elif Math_Marks >= 70:
    Math_Grade = "C"
elif Math_Marks >= 60:
    Math_Grade = "D"
elif Math_Marks >= 50:
    Math_Grade = "E"
elif Math_Marks >= 40:
    Math_Grade = "F"
else:
    Math_Grade = "Fail"


if English_Marks >= 90:
    English_Grade = "A"
elif English_Marks >= 80:
    English_Grade = "B"
elif English_Marks >= 70:
    English_Grade = "C"
elif English_Marks >= 60:
    English_Grade = "D"
elif English_Marks >= 50:
    English_Grade = "E"
elif English_Marks >= 40:
    English_Grade = "F"
else:
    English_Grade = "Fail"


if Sst_Marks >= 90:
    Sst_Grade = "A"
elif Sst_Marks >= 80:
    Sst_Grade = "B"
elif Sst_Marks >= 70:
    Sst_Grade = "C"
elif Sst_Marks >= 60:
    Sst_Grade = "D"
elif Sst_Marks >= 50:
    Sst_Grade = "E"
elif Sst_Marks >= 40:
    Sst_Grade = "F"
else:
    Sst_Grade = "Fail"


if Urdu_Sans_marks >= 90:
    Urdu_Sans_Grade = "A"
elif Urdu_Sans_marks >= 80:
    Urdu_Sans_Grade = "B"
elif Urdu_Sans_marks >= 70:
    Urdu_Sans_Grade = "C"
elif Urdu_Sans_marks >= 60:
    Urdu_Sans_Grade = "D"
elif Urdu_Sans_marks >= 50:
    Urdu_Sans_Grade = "E"
elif Urdu_Sans_marks >= 40:
    Urdu_Sans_Grade = "F"
else:
    Urdu_Sans_Grade = "Fail"

if Percentage >= 90:
    Overall_Grade = "A"
elif Percentage >= 80:
    Overall_Grade = "B"
elif Percentage >= 70:
    Overall_Grade = "C"
elif Percentage >= 60:
    Overall_Grade = "D"
elif Percentage >= 50:
    Overall_Grade = "E"
elif Percentage >= 40:
    Overall_Grade = "F"
else:
    Overall_Grade = "Fail"


print("\nStudent Name:",Student_Name)

print("\nScience:--------",Science_Marks
      ,"\nGrade:----------",Science_Grade)

print("\nMathematics:----",Math_Marks
      ,"\nGrade:----------",Math_Grade)

print("\nEnglish:--------",English_Marks
      ,"\nGrade:----------",English_Grade)

print("\nSocial Studies:-",Sst_Marks
      ,"\nGrade:----------",Sst_Grade)

print("\nUrdu/Sanskrit:--",Urdu_Sans_marks
      ,"\nGrade:----------",Urdu_Sans_Grade)

print("------------------------------\nTotal Marks:",Total_Marks,"\nPercentage:",Percentage, "\nOverall Grade:",Overall_Grade,"\n----------------------------")