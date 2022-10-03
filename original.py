# noinspection PyTypeChecker
def read_file(filename):
    lines = open(filename).read().splitlines()
    booking_table = [x.split(",") for x in lines if x != ""]
    for row in booking_table:
        row[0] = int(row[0])
        row[1] = int(row[1])
        row[3] = int(row[3])
        row[4] = int(row[4])
    return booking_table


def initialize_str_nested_list(num_rows, num_cols):
    return [['' for _ in range(num_cols)] for _ in range(num_rows)]


def initialize_int_nested_list(num_rows, num_cols):
    return [[0 for _ in range(num_cols)] for _ in range(num_rows)]


def get_booking_by_date(booking_table, num_floors, num_rooms, _date):
    curr_guests = initialize_str_nested_list(num_floors, num_rooms)
    curr_booking = initialize_int_nested_list(num_floors, num_rooms)

    for i in booking_table:
        if i[3] <= _date < i[4]:
            curr_booking[i[0] - 1][i[1] - 1] = 1
            curr_guests[i[0] - 1][i[1] - 1] = i[2]

    return curr_booking, curr_guests


def draw_booking(curr_booking):
    cell_width = 3
    cell_height = 3
    print('|', end='')
    for j in range(len(curr_booking[0]) + 1):
        print('-' * cell_width + '|', end='')
    print()
    print('|   |', end='')
    for j in range(len(curr_booking[0])):
        print(f'{j + 1:^3}|', end='')
    print()
    print('|', end='')
    for j in range(len(curr_booking[0]) + 1):
        print('-' * cell_width + '|', end='')
    print()

    for i in range(cell_height - 1):
        print(f'|{i:^{cell_width}}|', end='')
        for j in range(len(curr_booking[0])):
            n = ""
            if curr_booking[i][j] == 1:
                n = "X"
            print(f'{n:^{cell_width}}|', end='')
        print()
        print('|', end='')
        for j in range(len(curr_booking[0]) + 1):
            print('-' * cell_width + '|', end='')
        print()


def get_booked_room_info_by_date(curr_booking, curr_guests):
    booked_room = []
    for i in range(len(curr_booking)):
        for j in range(len(curr_booking[i])):
            if curr_booking[i][j] == 1:
                booked_room.append([i + 1, j + 1, curr_guests[i][j]])

    return booked_room


def display_available_rooms(curr_booking):
    available = "Available rooms: "
    for i in range(len(curr_booking)):
        for j in range(len(curr_booking[i])):
            if curr_booking[i][j] == 0:
                available += f"({i + 1},{j + 1}), "

    print(available[:-1])


def get_booked_room_info_by_floor(curr_booking, curr_guests, _floor):
    booked_room = []
    for i in range(len(curr_booking[_floor - 1])):
        if curr_booking[_floor - 1][i] == 1:
            booked_room.append([_floor, i + 1, curr_guests[_floor - 1][i]])

    return booked_room


def get_booked_room_info_by_name(curr_booking, curr_guests, _name):
    booked_room = []
    for i in range(len(curr_guests)):
        for j in range(len(curr_booking[i])):
            if _name in curr_guests[i][j]:
                booked_room.append([i + 1, j + 1, _name])

    return booked_room


def count_booked_room_by_date(booking_table, _date):
    return sum([1 for i in booking_table if i[3] <= _date < i[4]])


def get_daily_revenue(booking_table, start_date, end_date):
    return [sum([2500 for j in booking_table if j[3] <= i < j[4]]) for i in
            range(start_date, end_date + 1)]


def get_floor_revenue_by_date(booking_table, num_floors, current_date):
    return [sum([2500 for j in booking_table if
                 j[0] == i + 1 and j[3] <= current_date < j[4]]) for i in
            range(num_floors)]


def get_room_revenue_by_date(booking_table, num_rooms, current_date):
    return [sum([2500 for j in booking_table if
                 j[1] == i + 1 and j[3] <= current_date < j[4]]) for i in
            range(num_rooms)]


def operate(booking_table, num_floors, num_rooms, choice):
    if choice == 1:
        current_date = int(input('Enter date: '))
        curr_booking, curr_guests = get_booking_by_date(booking_table,
                                                        num_floors, num_rooms,
                                                        current_date)
        draw_booking(curr_booking)

    elif choice == 2:
        current_date = int(input('Enter date: '))
        curr_booking, curr_guests = get_booking_by_date(booking_table,
                                                        num_floors, num_rooms,
                                                        current_date)
        booked_room = get_booked_room_info_by_date(curr_booking, curr_guests)
        for i in booked_room:
            print(f"Room ({i[0]}, {i[1]}, {i[2]}), ")

    elif choice == 3:
        current_date = int(input('Enter date: '))
        curr_booking, curr_guests = get_booking_by_date(booking_table,
                                                        num_floors, num_rooms,
                                                        current_date)
        display_available_rooms(curr_booking)

    elif choice == 4:
        current_date = int(input('Enter date: '))
        curr_booking, curr_guests = get_booking_by_date(booking_table,
                                                        num_floors, num_rooms,
                                                        current_date)
        current_floor = int(input('Enter floor: '))
        booked_room = get_booked_room_info_by_floor(curr_booking, curr_guests,
                                                    current_floor)
        for i in booked_room:
            print(f"Room ({i[0]}, {i[1]}, {i[2]}), ")

    elif choice == 5:
        current_date = int(input('Enter date: '))
        curr_booking, curr_guests = get_booking_by_date(booking_table,
                                                        num_floors, num_rooms,
                                                        current_date)
        current_guest = input('Enter guest name: ')
        booked_room = get_booked_room_info_by_name(curr_booking, curr_guests,
                                                   current_guest)
        for i in booked_room:
            print(f"Room ({i[0]}, {i[1]}, {i[2]}), ")

    elif choice == 6:
        start_date = int(input('Enter start date: '))
        end_date = int(input('Enter end date: '))
        daily_revenue = get_daily_revenue(booking_table, start_date, end_date)
        for i in range(end_date - start_date + 1):
            print(f"{start_date + i}: {daily_revenue[i]} Baht")

    elif choice == 7:
        current_date = int(input('Enter date: '))
        floor_revenue = get_floor_revenue_by_date(booking_table, num_floors,
                                                  current_date)
        print(f"Revenue for date {current_date}")
        for i in range(len(floor_revenue)):
            print(f"Floor {i + 1}: {floor_revenue[i]} Baht")

    elif choice == 8:
        current_date = int(input('Enter date: '))
        room_revenue = get_room_revenue_by_date(booking_table, num_rooms,
                                                current_date)
        print(f"Revenue for date {current_date}")
        for i in range(len(room_revenue)):
            print(f"Room-Section {i + 1}: {room_revenue[i]} Baht")


# num_floors = 2
# num_rooms = 3
# booking_table = read_file('hotel_small.txt')
# print(booking_table)

# Uncomment below if you want to test with hotel.txt
num_floors = 3
num_rooms = 5
booking_table = read_file('hotel.txt')

print('1. Show booked rooms by date')
print('2. Show guest names by date')
print('3. Show available rooms by date')
print('4. Show booked rooms by floor')
print('5. Search booked room by name')
print('6. Show daily revenue')
print('7. Show floor revenue by date')
print('8. Show room-section revenue by date')
choice = int(input('Enter choice: '))
operate(booking_table, num_floors, num_rooms, choice)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
