number = int(input())
students = {}

for i in range(number):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)


for name, grade in students.items():
    grade = sum(grade) / len(grade)
    if grade >= 4.5:
        print(f"{name} -> {grade:.2f}")