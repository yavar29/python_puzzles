#program to interactively print the names of students, their grades, and missed assignments

names= input("enter comma separated names :")
assignments=input("enter missing assignments :")
grades=input("enter current grades :")

potential_grade=grades+ 2*assignments

names=names.split(",")
# print (type(names))
assignments=assignments.split(",")
grades=grades.split(",")
potential_grade.split(",")

for i in range(3):
    print( "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n".format(names[i],assignments[i],grades[i],potential_grade[i]))


