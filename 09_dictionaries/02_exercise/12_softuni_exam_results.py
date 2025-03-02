command = input()
results = {}
submissions = {}

while command != "exam finished":
    if command.count("-") == 1:
        username = command.split("-")[0]
        del results[username]
    elif command.count("-") == 2:
        username, language, points = command.split("-")
        points = int(points)
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
        if username not in results:
            results[username] = points
        else:
            if points > results[username]:
                results[username] = points

    command = input()


print("Results:")
for name, grade in results.items():
    print(f"{name} | {grade}")

print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")