path_to_a_file = input().split("\\")
file_name, extension = path_to_a_file[-1].split(".")
print(f"File name: {file_name}")
print(f"File extension: {extension}")