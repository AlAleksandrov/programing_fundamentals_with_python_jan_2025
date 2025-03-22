import re

def extract_function_names(string_):
    pattern = r"(=|\/)([A-Z][a-zA-Z]{2,})\1"
    matches = re.finditer(pattern, string_)
    function_names = [match.group(2) for match in matches]
    points = sum(len(name) for name in function_names)
    return function_names, points


string = input()
current_names, travel_points = extract_function_names(string)

print(f"Destinations: {', '.join(current_names)}")
print(f"Travel Points: {travel_points}")