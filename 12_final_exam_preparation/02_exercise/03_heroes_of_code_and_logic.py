def cast_spell(name_of_hero_, mana_points_, amount_, spell_name_):
    if mana_points_ - amount_ >= 0:
        mana_points_ -= amount_
        return mana_points_, f"{name_of_hero_} has successfully cast {spell_name_} and now has {mana_points_} MP!"
    else:
        return mana_points_, f"{name_of_hero_} does not have enough MP to cast {spell_name_}!"

def take_damage(name_of_hero_, hit_points_, damage_, attacker_):
    hit_points_ -= damage_
    if hit_points_ > 0:
        return hit_points_, f"{name_of_hero_} was hit for {damage_} HP by {attacker_} and now has {hit_points_} HP left!"
    else:
        hit_points_ = 0
        return hit_points_, f"{name_of_hero_} has been killed by {attacker_}!"

def recharge(name_of_hero_, mana_points_, amount_):
    amount_recovered = amount_
    mana_points_ += amount_
    if mana_points_ > 200:
        amount_recovered = amount_ - (mana_points_ - 200)
        mana_points_ = 200
    return mana_points_, f"{name_of_hero_} recharged for {amount_recovered} MP!"

def heal(name_of_hero_, hit_points_, amount_):
    hit_points_ += amount_
    amount_recovered = amount_
    if hit_points_ > 100:
        amount_recovered = amount_ - (hit_points_ - 100)
        hit_points_ = 100
    return hit_points_, f"{name_of_hero_} healed for {amount_recovered} HP!"

def main(number):
    heroes_dict = {}

    for _ in range(number):
        heroes_ = input()
        hero_name, hit_points, mana_points = heroes_.split()
        hit_points = min(int(hit_points), 100)
        mana_points = min(int(mana_points), 200)
        heroes_dict[hero_name] = {"HP": int(hit_points), "MP": int(mana_points)}

    while True:
        commands_ = input().split(" - ")
        command = commands_[0]
        if command == "End":
            return heroes_dict
        if command == "CastSpell":
            name_of_hero, amount, spell_name = commands_[1], int(commands_[2]), commands_[3]
            heroes_dict[name_of_hero]["MP"], current_result = cast_spell(name_of_hero, heroes_dict[name_of_hero]["MP"], amount, spell_name)
            print(current_result)
        elif command == "TakeDamage":
            name_of_hero, damage, attacker = commands_[1], int(commands_[2]), commands_[3]
            heroes_dict[name_of_hero]["HP"], current_result = take_damage(name_of_hero, heroes_dict[name_of_hero]["HP"], damage, attacker)
            if heroes_dict[name_of_hero]["HP"] == 0:
                del heroes_dict[name_of_hero]
            print(current_result)
        elif command == "Recharge":
            name_of_hero, amount = commands_[1], int(commands_[2])
            heroes_dict[name_of_hero]["MP"], current_result = recharge(name_of_hero, heroes_dict[name_of_hero]["MP"], amount)
            print(current_result)
        elif command == "Heal":
            name_of_hero, amount = commands_[1], int(commands_[2])
            heroes_dict[name_of_hero]["HP"], current_result = heal(name_of_hero, heroes_dict[name_of_hero]["HP"], amount)
            print(current_result)


number_of_heroes = int(input())
result = main(number_of_heroes)

for name, points in result.items():
    print(name)
    print(f" HP: {points['HP']}")
    print(f" MP: {points['MP']}")