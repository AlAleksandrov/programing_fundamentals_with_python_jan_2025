def add(music_library_, piece_, composer_,key_):
    if piece_ not in music_library_:
        music_library_[piece_] = {"composer": composer_, "key": key_}
        print(f"{piece_} by {composer_} in {key_} added to the collection!")
        return music_library_
    else:
        print(f"{piece_} is already in the collection!")

def remove(music_library_, piece_):
    if piece_ in music_library_:
        del music_library_[piece_]
        print(f"Successfully removed {piece_}!")
        return music_library_
    else:
        print(f"Invalid operation! {piece_} does not exist in the collection.")

def change_key(music_library_, piece_, new_key_):
    if piece_ in music_library_:
        music_library_[piece_]['key'] = new_key_
        print(f"Changed the key of {piece_} to {new_key_}!")
        return music_library_
    else:
        print(f"Invalid operation! {piece_} does not exist in the collection.")

def main(number_):
    music_library = {}
    for _ in range(number):
        initial_pieces = input().split("|")
        piece, composer, key = initial_pieces[0], initial_pieces[1], initial_pieces[2]
        music_library[piece] = {"composer": composer, "key": key}
    commands = input().split("|")
    while True:
        if commands[0] == "Stop":
            return music_library
        command = commands[0]
        if command == "Add":
            piece, composer, key = commands[1], commands[2], commands[3]
            add(music_library, piece, composer, key)
        elif command == "Remove":
            piece = commands[1]
            remove(music_library, piece)
        elif command == "ChangeKey":
            piece, new_key = commands[1], commands[2]
            change_key(music_library, piece, new_key)

        commands = input().split("|")


number = int(input())
result = main(number)
for pieces, details in result.items():
    composers = details["composer"]
    keys = details["key"]
    print(f"{pieces} -> Composer: {composers}, Key: {keys}")