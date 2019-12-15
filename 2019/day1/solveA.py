import sys

def main():
    total_fuel = 0
    for line in sys.stdin:
        total_fuel += (int(line.rstrip()) // 3) - 2
    print(total_fuel)



if __name__ == '__main__':
    main()
