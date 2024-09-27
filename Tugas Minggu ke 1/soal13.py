#predict sections in batch of student 
student = int(input('Enter enrolled student '))

left = student % 30 
section = (student - left) / 30 

print(f'Student Enrolled {student}')
print(f'Section will be required is {section} and number of student that will be left over is {left}')