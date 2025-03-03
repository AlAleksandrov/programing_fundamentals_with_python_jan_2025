command = input()
force_book= {}
names = []

while command != "Lumpawaroo":
    if " | " in command:
        force_side, force_user = command.split(" | ")
        if force_side not in force_book:
            force_book[force_side] = []
        if force_user not in names:
            names.append(force_user)
            force_book[force_side].append(force_user)

    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        if force_side not in force_book:
            force_book[force_side] = []

        for side in force_book:
            if force_user in force_book[side]:
                force_book[side].remove(force_user)

        force_book[force_side].append(force_user)
        if force_user not in names:
            names.append(force_user)

        print(f"{force_user} joins the {force_side} side!")

    command = input()


for force_side, force_users in force_book.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for force_user in force_users:
            print(f"! {force_user}")