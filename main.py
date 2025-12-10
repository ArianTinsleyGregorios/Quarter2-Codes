students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

totalclass = 0
totalscores = 0

for s in range(1, students + 1):
    print()
    print("Student", s)
    totalstudent = 0

    for sub in range(1, subjects + 1):
        score = float(input("Enter score " + str(sub) + ":"))
        totalstudent = totalstudent + score

    averagestudent = totalstudent / subjects
    print("Average for Student", s, "=", averagestudent)

    totalclass = totalclass + totalstudent
    totalscores = totalscores + subjects

classaverage = totalclass / totalscores
print()
print("Class Average =", classaverage)
