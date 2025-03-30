facebook = {}

while True:
    command = input()
    if command == 'Log out':
        break

    parts = command.split(":")
    parts = [p.strip() for p in parts]
    action = parts[0]

    if action == 'New follower':
        if len(parts) != 2:
            continue
        username = parts[1]
        if username not in facebook:
            facebook[username] = {'Likes': 0, 'Comments': 0}

    elif action == 'Like':
        if len(parts) != 3:
            continue
        username= parts[1]
        count = int(parts[2])
        if username not in facebook:
            facebook[username] = {'Likes': count, 'Comments': 0}
        else:
            facebook[username]['Likes'] += count

    elif action == 'Comment':
        if len(parts) != 2:
            continue
        username = parts[1]
        if username not in facebook:
            facebook[username] = {'Likes': 0, 'Comments': 1}
        else:
            facebook[username]['Comments'] += 1

    elif action == 'Blocked':
        if len(parts) != 2:
            continue
        username = parts[1]
        if username in facebook:
            del facebook[username]
        else:
            print(f"{username} doesn't exist.")


print(f"{len(facebook)} followers")
for username, info in facebook.items():
    total_count = info['Likes'] + info['Comments']
    print(f"{username}: {total_count}")