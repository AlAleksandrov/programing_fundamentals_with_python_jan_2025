def rate(plant_dict:float, new_rating:float) ->float:
    plant_dict += new_rating
    return plant_dict

def main(current_number:int) ->dict:
    plants_dict = {}
    plants_counter = {}

    for _ in range(current_number):
        plant, rarity = input().split("<->")
        if plant not in plants_dict:
            plants_dict[plant] = {"Rarity": int(rarity), "Rating": 0.0}
            plants_counter[plant] = {"Counter": 0}
        else:
            plants_dict[plant]["Rarity"] = int(rarity)

    while True:
        commands = input()
        if commands == "Exhibition":
            for plant_name in plants_dict:
                if plants_counter[plant_name]["Counter"] > 0:
                    plants_dict[plant_name]["Rating"] = plants_dict[plant_name]["Rating"] / plants_counter[plant_name]["Counter"]
            return plants_dict
        command, plant_info = commands.split(": ")
        if command == "Rate":
            plant_name, rating = plant_info.split(" - ")
            if plant_name not in plants_dict:
                print("error")
            else:
                plants_dict[plant_name]["Rating"] = rate(float(plants_dict[plant_name]["Rating"]), float(rating))
                plants_counter[plant_name]["Counter"] += 1
        elif command == "Update":
            plant_name, rarity = plant_info.split(" - ")
            if plant_name not in plants_dict:
                print("error")
            else:
                plants_dict[plant_name]["Rarity"] = int(rarity)
        elif command == "Reset":
            plant_name = plant_info
            if plant_name not in plants_dict:
                print("error")
            else:
                plants_dict[plant_name]["Rating"] = 0.0
                plants_counter[plant_name]["Counter"] = 0


number = int(input())
result = main(number)
print("Plants for the exhibition:")
for plants, results in result.items():
    print(f"- {plants}; Rarity: {results['Rarity']}; Rating: {results['Rating']:.2f}")