first_employee_help_per_hour = int(input())
second_employee_help_per_hour = int(input())
third_employee_help_per_hour = int(input())
students = int(input())
time = 0
add_time = 0
while students != 0:
    students_per_hour = first_employee_help_per_hour + second_employee_help_per_hour + third_employee_help_per_hour
    if students >= students_per_hour:
        students -= students_per_hour
        time += 1
    else:
        students = 0
        time += 1
        break
    if students > 0 and time % 3 == 0:
        add_time += 1
print(f"Time needed: {time + add_time}h.")