import sys

def parse_seat(seat):
    row_str = seat[:7]
    col_str = seat[7:]
    row = int(row_str.replace('F', '0').replace('B', '1'), 2)
    col = int(col_str.replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col

def main():
    max_seat_id = 0
    for line in sys.stdin:
        seat_id = parse_seat(line.rstrip())
        max_seat_id = max(max_seat_id, seat_id)

    print(max_seat_id)

if __name__ == '__main__':
    main()
