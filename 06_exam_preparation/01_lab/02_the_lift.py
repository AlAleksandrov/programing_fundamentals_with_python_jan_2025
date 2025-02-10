waiting_peoples_on_the_lift = int(input())
current_state = input().split()
number = 0

for state in range(len(current_state)):
    if current_state[state] == '0':
        if waiting_peoples_on_the_lift >= 4:
            number = 4
            current_state[state] = str(0 + number)
            waiting_peoples_on_the_lift -= number
        else:
            number = waiting_peoples_on_the_lift
            current_state[state] = str(0 + number)
            waiting_peoples_on_the_lift -= number
    elif current_state[state] == '1':
        if waiting_peoples_on_the_lift >= 4:
            number = 3
            current_state[state] = str(1 + number)
            waiting_peoples_on_the_lift -= number
        else:
            number = waiting_peoples_on_the_lift
            current_state[state] = str(1 + number)
            waiting_peoples_on_the_lift -= number
    elif current_state[state] == '2':
        if waiting_peoples_on_the_lift >= 4:
            number = 2
            current_state[state] = str(2 + number)
            waiting_peoples_on_the_lift -= number
        else:
            number = waiting_peoples_on_the_lift
            current_state[state] = str(2 + number)
            waiting_peoples_on_the_lift -= number
    elif current_state[state] == '3':
        if waiting_peoples_on_the_lift >= 4:
            number = 1
            current_state[state] = str(3 + number)
            waiting_peoples_on_the_lift -= number
        else:
            number = waiting_peoples_on_the_lift
            current_state[state] = str(3 + number)
            waiting_peoples_on_the_lift -= number
    elif current_state[state] == '4':
        continue
if waiting_peoples_on_the_lift == 0 and current_state[state] == str(4):
    print(" ".join(current_state))
elif waiting_peoples_on_the_lift == 0 and current_state[state] != str(4):
    print("The lift has empty spots!")
    print(" ".join(current_state))
elif waiting_peoples_on_the_lift != 0 and current_state[state] == str(4):
    print(f"There isn't enough space! {waiting_peoples_on_the_lift} people in a queue!")
    print(" ".join(current_state))