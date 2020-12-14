import sys


def vec_plus(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def vec_mult(v1, s):
    """Scalar multiplication"""
    return (v1[0] * s, v1[1] * s)

DIRS = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0),
}

TURN_RIGHT_ORDER = ['N', 'E', 'S', 'W']

class ShipNav:
    def __init__(self):
        self.direction = 'E'
        self.pos = (0, 0)

    def follow_inst(self, inst):
        inst, arg = inst[0], int(inst[1:])
        if inst in DIRS.keys():
            self.pos = vec_plus(self.pos, vec_mult(DIRS[inst], arg))
        if inst in ('R', 'L'):
            if inst == 'L':
                arg = -arg
            turns = arg // 90
            index = TURN_RIGHT_ORDER.index(self.direction)
            self.direction = TURN_RIGHT_ORDER[(index + turns) % len(TURN_RIGHT_ORDER)]
        if inst == 'F':
            self.pos = vec_plus(self.pos, vec_mult(DIRS[self.direction], arg))

    def manhattan_distance(self):
        return abs(self.pos[0]) + abs(self.pos[1])


def main():
    shipnav = ShipNav()
    for line in sys.stdin:
        shipnav.follow_inst(line.strip())
    print(shipnav.pos)
    print(shipnav.manhattan_distance())

if __name__ == '__main__':
    main()
