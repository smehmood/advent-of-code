import sys
import re

field_re = re.compile('(.*): (\d+)-(\d+) or (\d+)-(\d+)')

def parse_field(line):
    match = field_re.match(line)
    field_name, s1, e1, s2, e2 = match.groups()
    return (field_name, (int(s1), int(e1)), (int(s2), int(e2)))


def contains(_range, num):
    return _range[0] <= num <= _range[1]

def valid(valid_ranges, num):
    for _range in valid_ranges:
        if contains(_range, num):
            return True
        elif _range[0] > num:
            break
    return False


def main():
    found_nearby_tickets = False
    valid_ranges = []
    invalid_sum = 0
    section = 0
    for line in sys.stdin:
        line = line.rstrip()
        if line:
            if section == 0:
                field_name, range1, range2 = parse_field(line)
                valid_ranges.append(range1)
                valid_ranges.append(range2)
            if section == 1:
                continue
            if section == 2:
                if line == "nearby tickets:":
                    continue
                for num_str in line.split(","):
                    num = int(num_str)
                    if not valid(valid_ranges, num):
                        invalid_sum += num
        else:
            if section == 0:
                valid_ranges.sort()
            section += 1

    print(invalid_sum)




if __name__ == '__main__':
    main()
