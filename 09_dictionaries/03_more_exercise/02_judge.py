contests = {}
statistics = {}

while True:
    command = input()
    if command == "no more time":
        break

    username, contest, points = command.split(" -> ")
    points = int(points)
    if contest not in contests:
        contests[contest] = {username:points}
        if username not in statistics:
            statistics[username] = points
        else:
            statistics[username] += points
    else:
        if username not in contests[contest]:
            contests[contest][username] = points
            if username not in statistics:
                statistics[username] = points
            else:
                statistics[username] += points
        elif points > contests[contest][username]:
            statistics[username] -= contests[contest][username]
            statistics[username] += points
            contests[contest][username] = points


for keys in contests.keys():
    print(f"{keys}: {len(contests[keys])} participants")
    sorted_value = sorted(contests[keys].items(), key=lambda x: (-x[1], x[0]))
    y = 1
    for last_contest, point in sorted_value:
        print(f"{y}. {last_contest} <::> {point}")
        y += 1

print("Individual standings:")
sorted_value = sorted(statistics.items(), key=lambda x: (-x[1], x[0]))
z = 1
for last_contest, point in sorted_value:
    print(f"{z}. {last_contest} -> {point}")
    z += 1