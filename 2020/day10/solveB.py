import sys

def main():
    inp = [int(line.strip()) for line in sys.stdin]
    inp.append(0)  # no need to add the last device, it doesn't change the num paths
    inp.sort()
    pathCount = [0] * len(inp) # pathCount[i] is the number of paths to inp[1]
    pathCount[0] = 1
    for i in range(1, len(inp)):
        for lookback in range(1, 4):
            prior = i - lookback
            if prior < 0 or inp[i] - inp[prior] > 3:
                break
            pathCount[i] += pathCount[prior]
    print(pathCount[-1])

if __name__ == '__main__':
    main()
