import sys

def main():
    seen = set()
    sums = set()
    products = {}
    for line in sys.stdin:
        num = int(line.rstrip())
        if (2020 - num) in sums:
            print(num * products[2020-num])
            break
        for prior in seen:
            zum = prior + num
            if zum < 2020:
                sums.add(prior + num)
                products[prior + num] = prior * num
        seen.add(num)



if __name__ == '__main__':
    main()
