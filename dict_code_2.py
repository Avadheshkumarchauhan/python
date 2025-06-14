student_marks={
    'jenny':92,
    'harry':78,
    'avavdhesh':56,
    'amit':41,
    'prem':33,
    'ankit':99
}
for student in student_marks:
    mark=student_marks[student]
    if mark<=100 and mark>=90:
        student_marks[student]='A+'
    elif mark<90 and mark>=80:
        student_marks[student]='A'
    elif mark<80 and mark>=70:
        student_marks[student]='B+'
    elif mark<70 and mark>=60:
        student_marks[student]='B'
    elif mark<60 and mark>=50:
        student_marks[student]='c'
    elif mark<50 and mark>=40:
        student_marks[student]='d'
    else:
        student_marks[student]='f'
        
print(student_marks)