initial_list = list(map(int, input().split()))

while True:
    command = input().split()
    action = command[0]
    if action == "end":
        print(initial_list)
        break

    if action == "exchange":
        index = int(command[1])
        if 0 <= index < len(initial_list):
            initial_list = initial_list[index + 1:] + initial_list[:index + 1]
        else:
            print("Invalid index")

    elif action == "max":
        even_odd = command[1]

        if even_odd == "even":
            even_numbers = list(filter(lambda x: x % 2 == 0, initial_list))
            if even_numbers:
                max_even_number = max(even_numbers)
                current_index = max((i for i, n in enumerate(initial_list) if n == max_even_number))
                print(current_index)
            else:
                print("No matches")

        elif even_odd == "odd":
            odd_numbers = list(filter(lambda x: x % 2 != 0, initial_list))
            if odd_numbers:
                max_odd_number = max(odd_numbers)
                current_index = max((i for i, n in enumerate(initial_list) if n == max_odd_number))
                print(current_index)
            else:
                print("No matches")

    elif action == "min":
        even_odd = command[1]

        if even_odd == "even":
            even_numbers = list(filter(lambda x: x % 2 == 0, initial_list))
            if even_numbers:
                min_even_number = min(even_numbers)
                current_index = max((i for i, n in enumerate(initial_list) if n == min_even_number))
                print(current_index)
            else:
                print("No matches")

        elif even_odd == "odd":
            odd_numbers = list(filter(lambda x: x % 2 != 0, initial_list))
            if odd_numbers:
                min_odd_number = min(odd_numbers)
                current_index = max((i for i, n in enumerate(initial_list) if n == min_odd_number))
                print(current_index)
            else:
                print("No matches")

    elif action == "first":
        count, even_odd = int(command[1]), command[2]

        if even_odd == "even":
            even_numbers = list(filter(lambda x: x % 2 == 0, initial_list))
            if count > len(initial_list):
                print("Invalid count")
                continue
            if even_numbers:
                if count <= len(even_numbers):
                    even_numbers = even_numbers[:count]
                    print(even_numbers)
                else:
                    print(even_numbers)
            else:
                print("[]")

        elif even_odd == "odd":
            odd_numbers = list(filter(lambda x: x % 2 != 0, initial_list))
            if count > len(initial_list):
                print("Invalid count")
                continue
            if odd_numbers:
                if count <= len(odd_numbers):
                    odd_numbers = odd_numbers[:count]
                    print(odd_numbers)
                else:
                    print(odd_numbers)
            else:
                print("[]")

    elif action == "last":
        count, even_odd = int(command[1]), command[2]

        if even_odd == "even":
            even_numbers = list(filter(lambda x: x % 2 == 0, initial_list))
            if count > len(initial_list):
                print("Invalid count")
                continue
            if even_numbers:
                if count <= len(even_numbers):
                    even_numbers = even_numbers[-count:]
                    print(even_numbers)
                else:
                    print(even_numbers)
            else:
                print("[]")

        elif even_odd == "odd":
            odd_numbers = list(filter(lambda x: x % 2 != 0, initial_list))
            if count > len(initial_list):
                print("Invalid count")
                continue
            if odd_numbers:
                if count <= len(odd_numbers):
                    odd_numbers = odd_numbers[-count:]
                    print(odd_numbers)
                else:
                    print(odd_numbers)
            else:
                print("[]")