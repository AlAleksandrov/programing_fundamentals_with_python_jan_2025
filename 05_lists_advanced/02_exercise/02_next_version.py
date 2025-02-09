version = input()
version_digits_string = version.replace(".", "")
version_digit_integer = int(version_digits_string) + 1
version_digits_string = str(version_digit_integer)
print(".".join(version_digits_string))
