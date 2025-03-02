number = int(input())
parking = {}

for i in range(number):
    command = input().split()
    if command[0] == 'register':
        username, license_plate_number = command[1], command[2]
        if username not in parking:
            print(f"{username} registered {license_plate_number} successfully")
            parking[username] = license_plate_number
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")

    elif command[0] == 'unregister':
        username = command[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]


for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")