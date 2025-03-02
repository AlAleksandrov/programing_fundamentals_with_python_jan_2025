countries = input().split(", ")
capitals = input().split(", ")
my_dict = {key:value for key,value in zip(countries, capitals)}
for key, value in my_dict.items():
    print(f"{key} -> {value}")