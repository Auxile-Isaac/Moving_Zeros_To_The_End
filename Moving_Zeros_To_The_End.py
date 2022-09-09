def move_zeros(lst):
    for i in range(1, len(lst)+1):
        if lst[-i] == 0 and lst[-i] is not False:
            lst.append(lst.pop(-i))
    return lst