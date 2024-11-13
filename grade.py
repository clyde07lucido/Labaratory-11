grades = []

for i in range(5):
    while True:
        grade = float(input(f"Enter grade for student {i+1} (between 40-100): "))
        if 40 <= grade <= 100:
            grades.append(grade)
            break
        else:
            print("Invalid grade. It must be between 40 and 100. Please try again.")

average_grade = sum(grades) / len(grades)

passing_count = 0
for grade in grades:
    if grade >= 75:
        passing_count += 1

passing_percentage = (passing_count / len(grades)) * 100

print(f"\nAverage grade: {average_grade:.2f}")
print(f"Number of students with passing grade: {passing_count}")
print(f"Passing percentage: {passing_percentage:.2f}%")
print("Grades entered:", grades)