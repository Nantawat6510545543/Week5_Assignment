def get_booking_by_date(booking_table, num_floors, num_rooms, _date):
    """ From the given booking data from file, create 2 nested lists.  Each
        nested list has size = num_floors x num_rooms
    The first nested list shows which hotel room is booked on _date.
        Value = 1 if the room is booked. Otherwise, value = 0 for
        non-booked room.  For example, [[1, 0, 0], [0, 0, 1]] means that
        2 booked rooms are (floor 1, room 1) and (floor 2, room 3)
    The second nested list shows the guest names who books rooms on _date.
        For example [['Ann', '', ''], ['', '', 'Beth']] means that Ann books
        (floor 1, room 1) room, and Beth books (floor 2, room 3) room.

        :param booking_table: booking data from file
        :param num_floors: int
        :param num_rooms: int
        :param _date: int
        :return: two nested lists with size = num_rows x num_cols.
        The first nested list shows which hotel room is booked on _date
        The second nested list shows the guest names who books rooms on _date
        >>> get_booking_by_date([[1, 1, 'Ann', 21, 23], [2, 3, 'Beth', 22, 24]], 2, 3, 21)
        ([[1, 0, 0], [0, 0, 0]], [['Ann', '', ''], ['', '', '']])
        >>> get_booking_by_date([[1, 1, 'Ann', 21, 23], [2, 3, 'Beth', 22, 24]], 2, 3, 22)
        ([[1, 0, 0], [0, 0, 1]], [['Ann', '', ''], ['', '', 'Beth']])
        >>> get_booking_by_date([[1, 1, 'Ann', 21, 23], [2, 3, 'Beth', 22, 24]], 2, 3, 23)
        ([[0, 0, 0], [0, 0, 1]], [['', '', ''], ['', '', 'Beth']])
    """
    rooms = [[0 for j in range(num_rooms)] for i in range(num_floors)]

    for i in range(num_floors):
        for j in range(num_rooms):
            if booking_table[3] <= _date <= booking_table[5]:
                rooms[booking_table[0]][booking_table[1]] = 1
    print()
    return 0
