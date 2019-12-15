import sys

def main():
    total_fuel = 0
    for line in sys.stdin:
        mass = int(line.rstrip())
        while mass > 0:
            mass = (mass // 3) - 2
            total_fuel += max(mass, 0) 

    print(total_fuel)

if __name__ == '__main__':
    main()
