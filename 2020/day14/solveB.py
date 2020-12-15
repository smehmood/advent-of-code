import sys
import re

def generate_masks(mask):
    """Generates part1 masks from part2 masks"""
    mask = mask.replace('X', 'Y').replace('0', 'X')
    def subgen(mask):
        if 'Y' not in mask:
            yield mask
        else:
            yield from subgen(mask.replace('Y', '0', 1))
            yield from subgen(mask.replace('Y', '1', 1))

    yield from subgen(mask)

def apply_mask(mask, value):
    """ Applies mask using part 1 definition """
    set_ones_mask = int(''.join('0' if char in ('X', '0') else '1' for char in mask), 2)
    set_zeros_mask = int(''.join('1' if char in ('X', '1') else '0' for char in mask), 2)
    value |= set_ones_mask
    value &= set_zeros_mask
    return value

def test():
    mask = '000000000000000000000000000000X1001X'
    for m in generate_masks(mask):
        print(m)

def main():
    mask_re = re.compile('mask = ([X10]*)')
    mem_re = re.compile('mem\[(\d*)\] = (\d*)')

    mask = None
    mem = {}

    for line in sys.stdin:
        line = line.rstrip()
        match = mask_re.match(line)
        if match:
            mask = match.group(1)
            continue
        match = mem_re.match(line)
        if not match:
            sys.exit(f"Bad input line: {line}")
        addr, value = (int(x) for x in match.groups())
        for m in generate_masks(mask):
            mem[apply_mask(m, addr)] = value

    print(sum(mem.values()))

if __name__ == '__main__':
    main()
