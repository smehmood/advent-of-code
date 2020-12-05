import sys

def good_pw(pw_int):
    pw = str(pw_int)
    if len(pw) != 6:
        return False
    double = False
    decreasing = False
    last = None
    for char in pw:
        if last is not None and last > char:
            decreasing = True
            return False
        if last == char:
            double = True
        last = char

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
