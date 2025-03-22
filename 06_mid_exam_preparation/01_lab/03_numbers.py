sequence_of_integers = list(map(int, input().split()))
average = sum(sequence_of_integers) / len(sequence_of_integers)
numbers_greater_average = [number for number in sequence_of_integers if number > average]

if numbers_greater_average:
    five_nums = sorted(numbers_greater_average, reverse=True)[:5]
    print(" ".join(map(str, five_nums)))
else:
    print("No")