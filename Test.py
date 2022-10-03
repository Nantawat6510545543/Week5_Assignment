def get_booked_room_info_by_date(curr_booking, curr_guests):
    """ With two nested lists:
            The first nested list shows which hotel room is booked on
                specific _date,
            The second nested list shows the guest names who books rooms on
                specific _date
        Construct nested lists where each row contains 3 values: floor,
            room and guest name of the booked room.  See test outputs below.

        :param curr_booking: nested list of integers
        :param curr_guests: nested list of strings
        :return: nested lists where each row contains 3 values: floor, room and guest name of the booked room
        >>> get_booked_room_info_by_date([[1, 0, 0], [0, 0, 1]], [['Ann', '', ''], ['', '', 'Beth']])
        [[1, 1, 'Ann'], [2, 3, 'Beth']]
        >>> get_booked_room_info_by_date([[1, 0, 1], [0, 1, 0]], [['Ann', '', 'Beth'], ['', 'Cathy', '']])
        [[1, 1, 'Ann'], [1, 3, 'Beth'], [2, 2, 'Cathy']]
        >>> get_booked_room_info_by_date([[1, 1], [0, 1]], [['Charlie', 'David'], ['', 'Eric']])
        [[1, 1, 'Charlie'], [1, 2, 'David'], [2, 2, 'Eric']]
    """
    return [
        [[i + 1, j + 1, curr_guests[i][j]] for j in range(len(curr_booking[i]))
         if curr_booking[i][j] == 1] for i in range(len(curr_booking))]
