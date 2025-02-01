numbers = input().split()
rounded_numbers = []

for i in range(len(numbers)):
    rounded_numbers.append(int(round(float(numbers[i]), 0)))

print(rounded_numbers)