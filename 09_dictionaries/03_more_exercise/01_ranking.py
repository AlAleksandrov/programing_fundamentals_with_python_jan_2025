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
    if current_contest in first_dictionary and password == first_dictionary[current_contest]:
        if username not in second_dictionary:
            second_dictionary[username] = {current_contest:points}
            thirth_dictionary[username] = points
        else:
            if current_contest not in second_dictionary[username]:
                second_dictionary[username][current_contest] = points
                thirth_dictionary[username] += points
            elif points > second_dictionary[username][current_contest]:
                thirth_dictionary[username] = thirth_dictionary[username] - second_dictionary[username][current_contest] + points
                second_dictionary[username][current_contest] = points


total_points = 0
best_candidate = ""
for key, value in thirth_dictionary.items():
    if value > total_points:
        total_points = value
        best_candidate = key

print(f"Best candidate is {best_candidate} with total {total_points} points.")
print("Ranking:")

for name in sorted(second_dictionary.keys()):
    print(f"{name}")
    sorted_value = sorted(second_dictionary[name].items(), key=lambda x: (-x[1], x[0]))
    for last_contest, point in sorted_value:
        print(f"#  {last_contest} -> {point}")