# Шахматный «обед»

def can_eat(pos: (int, int), targ: (int, int)) -> bool:
    return abs(targ[0] - pos[0]) + abs(targ[1] - pos[1]) == 3
