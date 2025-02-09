number_of_rooms = int(input())
total_free_chairs = 0
for room in range(1, number_of_rooms + 1):
    chairs_in_the_rooms, visitors_in_the_rooms = input().split()
    chairs_in_the_room = len(chairs_in_the_rooms)
    visitors = int(visitors_in_the_rooms)
    chairs_in_room = chairs_in_the_room - visitors
    if chairs_in_room < 0:
        print(f'{abs(chairs_in_room)} more chairs needed in room {room}')
    total_free_chairs += chairs_in_room

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")