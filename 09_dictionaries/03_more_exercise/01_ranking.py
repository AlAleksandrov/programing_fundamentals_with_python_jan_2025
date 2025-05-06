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
    points = int(points)
    if current_contest in first_dictionary.keys() and password == first_dictionary[current_contest]:
        if username not in second_dictionary.keys():
            second_dictionary[username] = {current_contest:points}
        else:
            if current_contest not in second_dictionary[username].keys():
                second_dictionary[username][current_contest] = points
            else:
                if second_dictionary[username][current_contest] < points:
                    thirth_dictionary[username] += points - second_dictionary[username][current_contest]
                continue

        if username not in thirth_dictionary.keys():
            thirth_dictionary[username] = points
        else:
            thirth_dictionary[username] += points

total_points = 0
best_candidate = ""
for key, value in thirth_dictionary.items():
    if value > total_points:
        total_points = value
        best_candidate = key

print(f"Best candidate is {best_candidate} with total {total_points} points.")
print("Ranking:")
candidate = ""
for name, value in sorted(second_dictionary.items()):
    if name != candidate:
        print(f"{name}")
        candidate = name
    sorted_value = sorted(second_dictionary[name].items(), key=lambda x: (-x[1], x[0]))
    for last_contest, point in sorted_value:
        print(f"#  {last_contest} -> {point}")