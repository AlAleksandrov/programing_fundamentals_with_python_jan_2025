string = input()

for i, ch in enumerate(string):
    if ":" in ch:
        print(f":{string[i + 1]}")