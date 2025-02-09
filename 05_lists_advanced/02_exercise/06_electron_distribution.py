number_of_electrons = int(input())
filled_shells = []
counter = 0
while True:
    counter += 1
    electrons_per_shell = 2 * counter**2
    if electrons_per_shell < number_of_electrons:
        number_of_electrons -= electrons_per_shell
        filled_shells.append(electrons_per_shell)
    else:
        filled_shells.append(number_of_electrons)
        break
print(filled_shells)