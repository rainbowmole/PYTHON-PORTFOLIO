print("GRADES", "\n")

#Display
print('Grade', '\t', 'Equivalent Grade')
print('100-95', '\t', 'A')
print('94-90', '\t', 'B')
print('89-83', '\t', 'C')
print('82-75', '\t', 'D')
print('74 ↆ', '\t', 'F', '\n')
#Input
#Prelim Grade
PG = int(input('Enter Prelim Grades: '))
#Midterm Grade
MG = int(input('Enter Midterm Grades: '))
#Final Grade
FG = int(input('Enter Final Grade: '))

#Process
G = (PG+MG+FG)/3

#Output
print()
print('Grades is: ', G)
if G >= 95:
    print('The equivalent letter grade of', G, 'is A')
elif G >= 90:
    print('The equivalent letter grade of', G, 'is B')
elif G >= 83:
    print('The equivalent letter grade of', G, 'is C')
elif G >= 75:
    print('The equivalent letter grade of', G, 'is D')
elif G < 75:
    print('The equivalent letter grade of', G, 'is F')

