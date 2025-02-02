def winner_of_the_car_race(time:list) -> str:
    left_racer_times = []
    right_racer_times = []
    sum_time_left = 0
    sum_time_right = 0
    result = ""
    for left_index, time_left in enumerate(time):
        if left_index != len(time) // 2:
            left_racer_times.append(time_left)
            if int(time_left) != 0:
                sum_time_left += int(time_left)
            else:
                sum_time_left *= 0.8
        else:
            break
    for right_index in range(len(time) - 1, (len(time) // 2), -1):
            right_racer_times.append(time[right_index])
            if int(time[right_index]) != 0:
                sum_time_right += int(time[right_index])
            else:
                sum_time_right *= 0.8
    if sum_time_left < sum_time_right:
        result = f"The winner is left with total time: {sum_time_left:.1f}"
    elif sum_time_left > sum_time_right:
        result = f"The winner is right with total time: {sum_time_right:.1f}"
    return result


racers_time = input().split()
current_result =winner_of_the_car_race(racers_time)
print(current_result)