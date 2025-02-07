notes = []
to_do_notes = []
command = input()

while command != "End":
    notes.append(command)
    command = input()

notes = sorted(notes, key=lambda x: int(x.split('-')[0]))
for note in notes:
    digit = note.split('-')
    to_do_notes.append(digit[1])
print(to_do_notes)