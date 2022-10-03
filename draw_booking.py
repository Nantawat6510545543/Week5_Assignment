def draw_booking(curr_booking):
    """ Received the nested list shows which hotel room is booked on specific
    _date.
        Draw and show the booked hotel rooms according to choice 1.
        *** Partial code is given.  You also need to fill in some part on
        your own ***

        :param curr_booking: nested list shows which hotel room is booked on
                specific _date
        >>> draw_booking([[1, 0, 0], [0, 0, 0]])
        0
        >>> draw_booking([[1, 0, 0], [0, 0, 1]])
        0
        >>> draw_booking([[0, 0, 0], [0, 0, 1]])
        0
    """
    cell_width = 3
    cell_height = 2
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

    for i in range(cell_height):
        print(f'|{i:^3}|', end='')
        for j in range(len(curr_booking[0])):
            n = ""
            if curr_booking[i][j] == 1:
                n = "X"
            print(f'{n:^3}|', end='')
        print()
        print('|', end='')
        for j in range(len(curr_booking[0]) + 1):
            print('-' * cell_width + '|', end='')
        print()
