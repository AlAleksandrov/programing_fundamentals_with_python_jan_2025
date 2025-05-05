is_zero = False
negative_counter = 0

for _ in range(3):
    number = int(input())
    if number == 0:
        is_zero = True
        break
    elif number < 0:
        negative_counter += 1

if is_zero:
    print("zero")
else:
    if negative_counter % 2 == 0:
        print("positive")
    else:
        print("negative")