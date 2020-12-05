import sys

def main():
    seen = set()
    for line in sys.stdin:
        num = int(line.rstrip())
        if (2020 - num) in seen:
            print(num * (2020-num))
            break
        seen.add(num)

if __name__ == '__main__':
    main()
