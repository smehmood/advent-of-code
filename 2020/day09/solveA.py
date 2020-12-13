import sys
import argparse


def is_sum(num, window):
    # window size is short enough to not fuss with sets
    for i in range(len(window)):
        for j in range(len(window)):
            if i != j and window[i] + window[j] == num:
                return True
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--window-size',  type=int, default=25)
    args = parser.parse_args()

    window = []
    for line in sys.stdin:
        num = int(line.strip())
        if len(window) < args.window_size:
            window.append(num)
            continue
        if not is_sum(num, window):
            print(num)
            break
        window = window[1:] + [num]

if __name__ == '__main__':
    main()

