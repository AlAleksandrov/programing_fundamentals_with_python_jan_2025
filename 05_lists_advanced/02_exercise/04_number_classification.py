numbers = input().split(', ')
positive = [x for x in numbers if int(x) >= 0]
negative = [x for x in numbers if int(x) < 0]
even = [x for x in numbers if int(x) % 2 == 0]
odd = [x for x in numbers if int(x) % 2 != 0]
print("Positive: ",end=", ".join(positive))
print("\n""Negative: ",end=", ".join(negative))
print("\n""Even: ",end=", ".join(even))
print("\n""Odd: ",end=", ".join(odd))