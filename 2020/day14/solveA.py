import sys
import re

def apply_mask(mask, value):
    set_ones_mask = int(''.join('0' if char in ('X', '0') else '1' for char in mask), 2)
    set_zeros_mask = int(''.join('1' if char in ('X', '1') else '0' for char in mask), 2)
    value |= set_ones_mask
    value &= set_zeros_mask
    return value

def test():
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
    print(apply_mask(mask, 11))
    print(apply_mask(mask, 101))
    print(apply_mask(mask, 0))

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
        mem[addr] = apply_mask(mask, value)

    print(sum(mem.values()))

if __name__ == '__main__':
    main()
