grades = {
    "math" : 97,
    "english" : 93,
    "science" : 94,
    "gym" : 86,
    "history" : 85,
    "computer science" : 93,
    "home economics" : 90,
    "japanese" : 100
}

all_grades = grades.values()
classes = grades.keys()
total_grade = 0

for grade in all_grades:
    total_grade += grade

gpa = total_grade / len(classes)
highest_grade = max(all_grades)
highest_class = max(grades, key=grades.get)

print(f"Your GPA is {gpa}. Your highest grade was {highest_grade} in {highest_class}")