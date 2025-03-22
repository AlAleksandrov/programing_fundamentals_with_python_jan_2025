string_even_integers = list(map(int, input().split("@")))
command = input()
position = 0

while True:
    if command == "Love!":
        break
    else:
        command_parts = command.split()

    index = int(command_parts[1])
    position += index
    if position >= len(string_even_integers):
        position = 0
        if string_even_integers[position] == 0:
            print(f"Place {position} already had Valentine's day.")
        else:
            string_even_integers[position] -= 2
            if string_even_integers[position] == 0:
                print(f"Place {position} has Valentine's day.")

    else:
        if string_even_integers[position] == 0:
            print(f"Place {position} already had Valentine's day.")
        else:
            string_even_integers[position] -= 2
            if string_even_integers[position] == 0:
                print(f"Place {position} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {position}.")

failed_places = sum(1 for hearts in string_even_integers if hearts > 0)

if failed_places == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_places} places.")