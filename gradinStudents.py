'''Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the  and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.'''

def gradingStudents(grades):
    grade=grades
    print(grade)
    for i in grade:
        if i>35:
            j=i%10
            k=i//10
            z=k
            print(j,k)
            if j>5:
                z=k*10+10
                print(z)
            elif j<5:
                z=k*10+5
                print(z)
            if (z-i)<3 and (z-i)>0:
                grades[grades.index(i)]=z
                print('>3')
    return grade
print(gradingStudents([27,23,65,43,0,82,0]))