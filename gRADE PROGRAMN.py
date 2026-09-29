grade = input('Enter grade:')
grade = float(grade)
if grade>90:
    print('Your grade is A')
if grade>80 and grade<=90:
    print('Your grade is B')
if grade>=60 and grade<=80:
    print('Your grade is C')
if grade<60:
    print('Your grade is D')