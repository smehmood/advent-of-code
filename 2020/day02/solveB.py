import sys

def main():
    num_valid = 0
    for line in sys.stdin:
        rule, password = line.split(": ")
        letter = rule[-1]
        pos1, pos2 = map(int, rule[:-2].split("-"))
        if (password[pos1-1] == letter) != (password[pos2-1] == letter):
            num_valid += 1
    print(num_valid)


if __name__ == '__main__':
    main()
