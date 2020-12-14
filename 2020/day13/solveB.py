import sys

def solve(r1, m1, r2, m2):
    """Solve x = r1 mod m1; x = r2 mod m2"""
    inc = 0
    while True:
        guess = (r1 + m1 * inc)
        if guess % m2 == r2:
            return guess
        inc += 1

def main():
    _ = int(sys.stdin.readline().strip())
    bus_id_string = sys.stdin.readline().strip()
    zipped = [(int(bus_id), offset) for offset, bus_id in enumerate(bus_id_string.split(",")) if bus_id != 'x']
    moduli = [x[0] for x in zipped]
    residues = [(moduli[i] - x[1]) % moduli[i] for i, x in enumerate(zipped)]

    r = residues[0]
    m = moduli[0]
    for i in range(1, len(moduli)):
        r = solve(r, m, residues[i], moduli[i])
        m *= moduli[i]

    print(r)

if __name__ == '__main__':
    main()
