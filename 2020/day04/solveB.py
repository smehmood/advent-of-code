import re
import sys

class ValidationError(Exception):
    pass

def main():
    passport = {}
    num_valid = 0

    def process_passport():
        nonlocal passport
        nonlocal num_valid
        try:
            if not (1920 <= int(passport['byr']) <= 2002):
                raise ValidationError
            if not (2010 <= int(passport['iyr']) <= 2020):
                raise ValidationError
            if not (2020 <= int(passport['eyr']) <= 2030):
                raise ValidationError

            hgt = passport['hgt']
            hgt_num, hgt_unit = int(hgt[:-2]), hgt[-2:]

            if hgt_unit not in ('cm', 'in'):
                raise ValidationError
            if hgt_unit == 'cm' and not (150 <= hgt_num <= 193):
                raise ValidationError
            if hgt_unit == 'in' and not (59 <= hgt_num <= 76):
                raise ValidationError

            if not re.fullmatch('#[0-9a-f]{6}', passport['hcl']):
                raise ValidationError

            if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                raise ValidationError

            if not re.fullmatch('[0-9]{9}', passport['pid']):
                raise ValidationError

            num_valid += 1

        except (ValueError, KeyError, ValidationError):
            pass
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
