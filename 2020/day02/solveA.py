import sys

def main():
    num_valid = 0
    for line in sys.stdin:
        rule, password = line.split(": ")
        letter = rule[-1]
        _min, _max = map(int, rule[:-2].split("-"))
        letter_count = password.count(letter)
        if letter_count >= _min and letter_count <= _max:
            num_valid += 1
    print(num_valid)


if __name__ == '__main__':
    main()
