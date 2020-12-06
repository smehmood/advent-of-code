import sys

def main():
    group = None
    total = 0

    for line in sys.stdin:
        line = line.rstrip()
        if not line:
            total += len(group)
            group = None
            continue
        if group is None:
            group = set(line)
        else:
            group &= set(line)

    if line:
        total += len(group)
    print(total)

if __name__ == '__main__':
    main()
