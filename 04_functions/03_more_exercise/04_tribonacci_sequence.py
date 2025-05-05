tribonacci_sequence = []
def tribonacci(current_number):
    for num in range(current_number):
        if num == 0:
            tribonacci_sequence.append(str(num + 1))
        elif num == 1 or num == 2:
            tribonacci_sequence.append(str(num))
        else:
            sum = 0
            sum = int(tribonacci_sequence[num - 1]) + int(tribonacci_sequence[num - 2]) + int(tribonacci_sequence[num - 3])
            tribonacci_sequence.append(str(sum))
    return tribonacci_sequence


number = int(input())
result = tribonacci(number)
print(" ".join(result))