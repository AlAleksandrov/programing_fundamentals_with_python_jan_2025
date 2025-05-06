format_one = {}
format_two = {}

while True:
    command = input()
    if command == "Season end":
        break

    if " -> " in command:
        username, position, skill = command.split(" -> ")
        skill = int(skill)

        if username not in format_one:
            format_one[username] = {position:skill}
            format_two[username] = skill
        else:
            if position not in format_one[username]:
                format_one[username][position] = skill
                format_two[username] += skill
            elif skill > format_one[username][position]:
                format_two[username] -= format_one[username][position]
                format_two[username] += skill
                format_one[username][position] = skill

    elif " vs " in command:
        player_one, player_two  = command.split(" vs ")
        if player_one in format_one and player_two in format_one:
            common_positions = set(format_one[player_one].keys()) & set(format_one[player_two].keys())
            if common_positions:
                if format_two[player_one] > format_two[player_two]:
                    del format_one[player_two]
                    del format_two[player_two]
                elif format_two[player_one] < format_two[player_two]:
                    del format_one[player_one]
                    del format_two[player_one]


sorted_format_two = sorted(format_two.items(), key=lambda x: (-x[1], x[0]))
for player, total_skills in sorted_format_two:
    print(f"{player}: {total_skills} skill")
    sorted_format_one = sorted(format_one[player].items(), key=lambda y: (-y[1], y[0]))
    for current_position, current_skill in sorted_format_one:
        print(f"- {current_position} <::> {current_skill}")