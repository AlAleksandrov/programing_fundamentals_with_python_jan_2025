key = int(input())
number_of_lines = int(input())
ascii_number = 0
for i in range(number_of_lines):
    letters = input()
    ascii_number = ord(letters) + key
    print(chr(ascii_number), end = "")