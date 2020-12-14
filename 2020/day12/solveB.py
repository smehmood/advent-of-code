import sys


def vec_plus(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def vec_mult(v1, s):
    """Scalar multiplication"""
    return (v1[0] * s, v1[1] * s)

def turn_right(v):
    return (v[1], -v[0])
DIRS = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0),
}

TURN_RIGHT_ORDER = ['N', 'E', 'S', 'W']

class ShipNav:
    def __init__(self):
        self.pos = (0, 0)
        self.wp = (10, 1)

    def follow_inst(self, inst):
        inst, arg = inst[0], int(inst[1:])
        if inst in DIRS.keys():
            self.wp = vec_plus(self.wp, vec_mult(DIRS[inst], arg))
        if inst in ('R', 'L'):
            if inst == 'L':
                arg = 3 * arg # cheap way to avoid managing turning left
            turns = arg // 90
            for i in range(turns):
                self.wp = turn_right(self.wp)
        if inst == 'F':
            self.pos = vec_plus(self.pos, vec_mult(self.wp, arg))

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
