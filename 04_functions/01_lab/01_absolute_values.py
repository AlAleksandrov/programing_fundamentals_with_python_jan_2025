sequence_of_numbers = input().split()
absolute_values = []

for i in range(len(sequence_of_numbers)):
    absolute_values.append(abs(float(sequence_of_numbers[i])))

print(absolute_values)