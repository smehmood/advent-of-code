import sys

def find_nth(starting, n):
    last_turn = {num: i for i, num in enumerate(starting)}
    last_spoken = None
    for i in range(len(starting), n):
        ith = 0 if last_spoken not in last_turn else (i-1) - last_turn[last_spoken]
        last_turn[last_spoken] = i-1
        last_spoken = ith

    return ith

def main():
    starting = [int(x) for x in sys.stdin.readline().split(',')]
    print(find_nth(starting, 30000000))

if __name__ == '__main__':
    main()
