def loading_bar(some_number:int) -> str:
    loaded_percent = some_number // 10
    loaded_dots = 10 - loaded_percent
    if some_number == 100:
        result = "100% Complete!\n""[%%%%%%%%%%]"
    else:
        result = f"{some_number}% " \
        f"[{'%' * loaded_percent}{'.' * loaded_dots}]" \
        f"\nStill loading..."
    return result


number = int(input())
current_result = loading_bar(number)
print(current_result)