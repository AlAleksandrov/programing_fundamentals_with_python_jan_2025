phonebook = {}

while True:
    entry = input()
    if "-" not in entry:
        break
    phone_name, phone_number = entry.split("-")
    phonebook[phone_name] = phone_number

number = int(entry)
for _ in range(number):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")