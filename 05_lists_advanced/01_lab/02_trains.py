number = int(input())
train = [0] * number

while True:
    command = input().split()
    if command[0] == "add":
        train[- 1] += int(command[1])
    elif command[0] == "insert":
        train[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        train[int(command[1])] -= int(command[2])
    elif command[0] == "End":
        print(train)
        break