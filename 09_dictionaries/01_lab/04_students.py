students = []
while True:
    student = input()
    if ":" not in student:
        for i in students:
            name, ID, course = i[0], i[1], i[2]
            if student.startswith(course.split()[0]):
                print(f"{name} - {ID}")
        break
    else:
        students.append(student.split(":"))