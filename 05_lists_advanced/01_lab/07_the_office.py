employees_happiness = input().split()
happiness_improvement_factor = int(input())
employees_improvement_happiness = list(map(lambda x: int(x) * happiness_improvement_factor, employees_happiness))
employees_filtered = list(filter(lambda x: x >= sum(employees_improvement_happiness)/len(employees_improvement_happiness), employees_improvement_happiness))
if len(employees_filtered) >= len(employees_improvement_happiness) / 2:
    print(f"Score: {len(employees_filtered)}/{len(employees_improvement_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(employees_filtered)}/{len(employees_improvement_happiness)}. Employees are not happy!")