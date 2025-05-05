first_dictionary = {}
second_dictionary = {}
thirth_dictionary = {}

while True:
    command = input()
    if command == "end of contests":
        break
    contest, password_for_contest = command.split(":")
    first_dictionary[contest] = password_for_contest

while True:
    next_command = input()
    if next_command == "end of submissions":
        break
    current_contest, password, username, points = next_command.split("=>")
    if current_contest in first_dictionary.keys():
        if password in first_dictionary[current_contest]:
            if username + "|" + current_contest not in second_dictionary.keys():
                second_dictionary[username + "|" + current_contest] = points
                if username not in thirth_dictionary.keys():
                    thirth_dictionary[username] = int(points)
                else:
                    thirth_dictionary[username] += int(points)
            else:
                if int(points) > int(second_dictionary[username + "|" + current_contest]):
                    second_dictionary[username + "|" + current_contest] = points
                    thirth_dictionary[username] += (int(points) - int(second_dictionary[username + "|" + current_contest]))


total_points = 0
candidate = ""
for key, value in thirth_dictionary.items():
    if total_points < value:
        total_points = value
        candidate = key

print(f"Best candidate is {candidate} with total {total_points} points.")
print("Ranking:")
dictionary = {}
candidate = ""
for keys, values in sorted(second_dictionary.items()):
    name, last_contest = keys.split("|")
    if name != candidate:
        print(f"{name}")
        candidate = name
    print(f"#  {last_contest} -> {values}")