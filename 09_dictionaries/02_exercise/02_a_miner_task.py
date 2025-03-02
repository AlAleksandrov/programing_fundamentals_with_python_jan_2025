resources = {}
command = input()

while True:
    if command == 'stop':
        break
    resource = command
    command = input()
    quantity = int(command)
    if resource not in resources:
        resources[resource] = 0
    resources[resource] += quantity
    command = input()

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")