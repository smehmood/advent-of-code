import sys


def contains(s1, p1):
    low = min(s1[0], s1[1])
    high = max(s1[0], s1[1])
    return p1 >= low and p1 <= high

def intersect(s1, s2): 
    s1_src = s1[0] 
    s1_dst = s1[1] 
    s2_src = s2[0] 
    s2_dst = s2[1] 

    s1_is_horizontal = is_horizontal(s1_src, s1_dst)
    s2_is_horizontal = is_horizontal(s2_src, s2_dst)

    if s1_is_horizontal != s2_is_horizontal:
        if s1_is_horizontal:
            h, v = s1, s2
        else:
            h, v = s2, s1
         
        h_y = h[0][1]
        v_x = v[0][0]

        if contains((v[0][1], v[1][1]), h_y) and contains((h[0][0], h[1][0]), v_x):
            return (v_x, h_y)
    if s1_is_horizontal:
        if s1_src[1] != s2_src[1]:
            return None
        if contains((s1_src[0], s1_dst[0]), s2_src[0]) or contains((s1_src[0], s1_dst[0]), s2_dst[0]):
            return (min(s1_src[0], s1_dst[0], s2_src[0], s2_dst[0]),  s1_src[1])
    else:
        if s1_src[0] != s2_src[0]:
            return None
        if contains((s1_src[1], s1_dst[1]), s2_src[1]) or contains((s1_src[1], s1_dst[1]), s2_dst[1]):
            return (s1_src[0], min(s1_src[1], s1_dst[1], s2_src[1], s2_dst[1]))

def is_horizontal(p1, p2):
    return p1[1] == p2[1]

def is_vertical(p1, p2):
    return p1[0] == p2[0]

def dst(pt):
    return abs(pt[0]) + abs(pt[1])

def min_pt(pt1, pt2):
    if pt1 is None:
        return pt2
    if pt2 is None:
        return pt1
    if dst(pt1) < dst(pt2):
        return pt1 
    else:
        return pt2


class Wire(object):
    def __init__(self, path_str):
        self.path = [(0,0)]
        instructions = path_str.split(",")
        for inst in instructions:
            self.add_point(inst)

    def add_point(self, instruction):
        current = self.path[-1]  
        direction = instruction[0]
        length = int(instruction[1:])
        advance = None
        if direction == 'R':
            advance = lambda pt, x: (pt[0] + x, pt[1])
        if direction == 'L':
            advance = lambda pt, x: (pt[0] - x, pt[1])
        if direction == 'U':
            advance = lambda pt, x: (pt[0], pt[1] + x)
        if direction == 'D':
            advance = lambda pt, x: (pt[0], pt[1] - x)
        self.path.append(advance(current, length))

def main():
    path1 = sys.stdin.readline().rstrip()
    path2 = sys.stdin.readline().rstrip()

    wire1 = Wire(path1)
    wire2 = Wire(path2)

    closest_crossing = None

    for i, i_src in enumerate(wire1.path):
        i_dst = wire1.path[i+1] if i+1 < len(wire1.path) else None
        if i_dst is None:
            break
        for j, j_src in enumerate(wire2.path):
            j_dst = wire2.path[j+1] if j+1 < len(wire2.path) else None
            if j_dst is None:
                break

            crossing = intersect( (i_src, i_dst), (j_src, j_dst) )
            if crossing:
                print(crossing)

            if crossing == (0, 0):
                continue
            closest_crossing = min_pt(closest_crossing, crossing)


    print(dst(closest_crossing))



if __name__ == '__main__':
    main()
