command = input()
company_users = {}

while command != "End":
    company_name, employees_id = command.split(" -> ")
    if company_name not in company_users:
        company_users[company_name] = []
    if employees_id not in company_users[company_name]:
        company_users[company_name].append(employees_id)

    command = input()


for company, employees in company_users.items():
    print(f"{company}")
    for employee_id in employees:
        print(f"-- {employee_id}")