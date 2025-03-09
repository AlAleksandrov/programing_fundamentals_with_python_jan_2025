tickets = input().split(", ")
lucky_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    ticket = ticket.strip()

    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left_side = ticket[:10]
    right_side = ticket[10:]
    jackpot = False
    match_found = False

    for symbol in lucky_symbols:
        left_count = 0
        current_count = 0
        for char in left_side:
            if char == symbol:
                current_count += 1
                left_count = max(left_count, current_count)
            else:
                current_count = 0

        right_count = 0
        current_count = 0
        for char in right_side:
            if char == symbol:
                current_count += 1
                right_count = max(right_count, current_count)
            else:
                current_count = 0

        if left_count >= 6 and right_count >= 6:
            match_length = min(left_count, right_count)
            if match_length == 10:
                jackpot = True
            match_found = True
            break

    if jackpot:
        print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
    elif match_found:
        print(f'ticket "{ticket}" - {match_length}{symbol}')
    else:
        print(f'ticket "{ticket}" - no match')