new_string = input()
counter = 0
current_string = new_string.lower()

if "Sand".lower() in current_string:
      #  current_string.replace("sand","")
    counter += current_string.count("sand")
if "Water".lower() in current_string:
      #  current_string.replace("water", "")
    counter += current_string.count("water")
if "Fish".lower() in current_string:
      #  current_string.replace("fish", "")
    counter += current_string.count("fish")
if "Sun".lower() in current_string:
      #  current_string.replace("sun", "")
    counter += current_string.count("sun")
print(counter)