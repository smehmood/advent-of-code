import sys

def parse_seat(seat):
    row_str = seat[:7]
    col_str = seat[7:]
    row = int(row_str.replace('F', '0').replace('B', '1'), 2)
    col = int(col_str.replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col

def main():
    max_seat_id = 0
    seats = sorted([parse_seat(line.rstrip()) for line in sys.stdin])
    for i in range(len(seats)):
        if i == 0:
            continue
        if seats[i] - seats[i-1] == 2:
            print(seats[i] - 1)

if __name__ == '__main__':
    main()
