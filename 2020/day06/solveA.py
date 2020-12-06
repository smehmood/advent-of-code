import sys

def main():
    group = set()
    total = 0

    for line in sys.stdin:
        line = line.rstrip()
        if not line:
            total += len(group)
            group = set()
        group.update(line)
    if line:
        total += len(group)
    print(total)

if __name__ == '__main__':
    main()
