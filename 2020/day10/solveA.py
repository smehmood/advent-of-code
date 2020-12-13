import sys


def main():
    inp = [int(line.strip()) for line in sys.stdin]
    inp.sort()
    prior = 0
    ones = 0
    threes = 1 # for the last adaptor
    for i in inp:
        if i - prior == 1:
            ones += 1
        elif i - prior == 2:
            print("Two!")
        elif i - prior == 3:
            threes += 1
        else:
            print(i, prior)
            sys.exit("Bad input")
        prior = i

    print(ones * threes)

if __name__ == '__main__':
    main()
