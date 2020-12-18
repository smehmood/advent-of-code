import sys
import re

field_re = re.compile('(.*): (\d+)-(\d+) or (\d+)-(\d+)')

class Field:
    def __init__(self, line):
        match = field_re.match(line)
        field_name, s1, e1, s2, e2 = match.groups()
        self.field_name = field_name
        self.range1 = (int(s1), int(e1))
        self.range2 = (int(s2), int(e2))

    def valid(self, value):
        return contains(self.range1, value) or contains(self.range2, value)

    def str(self):
        return self.field_name

    def repr(self):
        return self.str()


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
    fields = []
    field_possibilities = None
    my_ticket = None

    for line in sys.stdin:
        line = line.rstrip()
        if line:
            if section == 0:
                field = Field(line)
                fields.append(field)
                valid_ranges.append(field.range1)
                valid_ranges.append(field.range2)
            if section == 1:
                if line == 'your ticket:':
                    continue
                my_ticket = [int(x) for x in line.split(',')]
                field_possibilities = [set(fields) for i in range(len(my_ticket))]
            if section == 2:
                if line == "nearby tickets:":
                    continue
                ticket = [int(x) for x in line.split(',')]
                invalid = False
                for field_value in ticket:
                    if not valid(valid_ranges, field_value):
                        invalid_sum += field_value
                        invalid = True
                if not invalid:
                    for i, field_value in enumerate(ticket):
                        possibilities = field_possibilities[i].copy()
                        for possibility in possibilities:
                            if not possibility.valid(field_value):
                                print(possibility.field_name)
                                field_possibilities[i].remove(possibility)
        else:
            if section == 0:
                valid_ranges.sort()
            section += 1


    while True:
        all_ones = True
        for possibilities in field_possibilities:
            if len(possibilities) > 1:
                all_ones = False
            elif len(possibilities) == 1:
                to_remove = next(iter(possibilities))
                for p in field_possibilities:
                    if p == possibilities:
                        continue
                    if to_remove in p:
                        p.remove(to_remove)
        if all_ones == True:
            break

    print([[f.field_name for f in fields] for fields in field_possibilities if len(fields) == 1])
    answer = 1
    for i, value in enumerate(my_ticket):
        if field_possibilities[i].pop().field_name.startswith("departure"):
            answer *= value

    print(invalid_sum)
    print(answer)




if __name__ == '__main__':
    main()
