number = int(input())
positive_numbers_list = []
negative_numbers_list = []
count_positive_numbers = 0
sum_of_negative_numbers = 0

for index in range(number):
    numbers = int(input())
    if numbers >= 0:
        positive_numbers_list.append(numbers)
        count_positive_numbers += 1
    else:
        negative_numbers_list.append(numbers)
        sum_of_negative_numbers += numbers

print(positive_numbers_list)
print(negative_numbers_list)
print(f"Count of positives: {count_positive_numbers}")
print(f"Sum of negatives: {sum_of_negative_numbers}")