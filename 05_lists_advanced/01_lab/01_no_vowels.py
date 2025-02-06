text = input()

new_string = [x for x in text if x.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(new_string))