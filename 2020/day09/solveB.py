import sys
import argparse


def is_sum(num, window):
    # window size is short enough to not fuss with sets
    for i in range(len(window)):
        for j in range(len(window)):
            if i != j and window[i] + window[j] == num:
                return True
    return False

def find_invalid(inp, window_size):
    window = []
    for num in inp:
        if len(window) < window_size:
            window.append(num)
            continue
        if not is_sum(num, window):
            return num
        window = window[1:] + [num]

def find_weakness(inp, target):
    assert target
    if not inp:
        return None
    start_index = 0
    end_index = 0
    acc = inp[start_index] = 0
    while start_index < len(inp) and end_index < len(inp):
        if acc < target or start_index == end_index:
            end_index += 1
            acc += inp[end_index]
        elif acc > target:
            acc -= inp[start_index]
            start_index += 1
        if acc == target:
            acc_check = 0
            for i in range(start_index, end_index + 1):
                acc_check += inp[i]
            acc_range = inp[start_index:end_index+1]
            return min(acc_range) + max(acc_range)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--window-size', type=int, default=25)
    args = parser.parse_args()

    inp = [int(line.strip()) for line in sys.stdin]
    invalid = find_invalid(inp, args.window_size)
    print(find_weakness(inp, invalid))

if __name__ == '__main__':
    main()

