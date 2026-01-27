# start
index = 0
total_grade = 0
students_count = int(input("how many students? "))
while index != students_count:
    grade = int(input("enter grade: "))
    if grade > 100 or grade < 0:
        continue
    index = index + 1
    total_grade = total_grade + grade
print("the average grade is:", total_grade / students_count)
