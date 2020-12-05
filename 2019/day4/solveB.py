import sys

def good_pw(pw_int):
    pw = str(pw_int)
    if len(pw) != 6:
        return False
    run_length = 1
    double = False
    last = None
    for char in pw:
        if last is not None and last > char:
            return False
        if last == char:
            run_length += 1
        else:
            if run_length == 2:
                double = True
            run_length = 1
        # print(last, char, run_length)
        last = char

    if run_length == 2:
        double = True

    return double


def main():
    range_string = sys.stdin.readline()
    start, end = [int(x) for x in range_string.split("-")]
    num_valid = 0
    for number in range(start, end):  # puzzle is ambiguous on inclusive/exclusive
        if good_pw(number):
            num_valid += 1
            print(number)

    print(num_valid)

if __name__ == "__main__":
    main()
