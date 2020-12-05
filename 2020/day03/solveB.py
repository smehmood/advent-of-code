import sys
from math import prod

def main():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    pos = [0] * len(slopes)
    num_trees = [0] * len(slopes)
    line_num = 0
    for line in sys.stdin:
        for i, slope in enumerate(slopes):
            if line_num % slope[1] != 0:
                continue
            if line[pos[i]] == '#':
                num_trees[i] += 1
            pos[i] = (pos[i] + slope[0]) % (len(line) - 1)  # minus 1 because of \n
        line_num += 1
    print(num_trees)
    print(prod(num_trees))

if __name__ == '__main__':
    main()
