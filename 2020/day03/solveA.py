import sys

def main():
    field = []
    pos = 0
    num_trees = 0
    for line in sys.stdin:
        if line[pos] == '#':
            num_trees += 1
        pos = (pos + 3) % (len(line) - 1)  # minus 1 because of \n
    print(num_trees)

if __name__ == '__main__':
    main()
