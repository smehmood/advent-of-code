import sys

def main():
    passport = {}
    num_valid = 0

    def process_passport():
        nonlocal passport
        nonlocal num_valid
        if 'cid' in passport:
            del passport['cid']
        num_valid += 1 if len(passport) == 7 else 0
        passport = {}

    for line in sys.stdin:
        if line == '\n':
            process_passport()
        fields = line.split()
        for field in fields:
            key, value = field.split(':')
            passport[key] = value
    if passport:
        process_passport()
    print(num_valid)

if __name__ == '__main__':
    main()
