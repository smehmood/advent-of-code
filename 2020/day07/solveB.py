""" Super hacky code, written to get an answer fast"""

from collections import defaultdict
import sys


class BagRules:
    """Ignores numbers since I don't think they're needed for part 1?"""
    def __init__(self):
        self.contains = defaultdict(lambda: (0, set()))  # key is contained by value

    def set_contains(self, a, b_list):
        """a bags contain X b1 bags, Y b2 bags, Z b3 bags"""
        total_bags = 0
        contains_set = set()
        for b in b_list:
            total_bags += b[0]
            contains_set.add(b)
        self.contains[a] = (total_bags, contains_set)

    def find_num_inner_bags(self, color):
        to_ret = self.contains[color][0]
        for c in self.contains[color][1]:
            to_ret += c[0] * self.find_num_inner_bags(c[1])

        return to_ret

def parse_bag(bag_string):
    return bag_string.rstrip().rsplit(' ', 1)[0]

def parse_inner_bag(inner_bag_string):
    int_str, bag_color = inner_bag_string.rstrip().rsplit(' ', 1)[0].split(' ', 1)
    return (int(int_str), bag_color)

def parse_graph(stream):
    bag_rules = BagRules()
    for line in stream:
        line = line.rstrip().rstrip(".")
        container_bag_str, inner_bag_str = line.split(" contain ")
        container_bag = parse_bag(container_bag_str)
        inner_bag_list = [] if inner_bag_str == "no other bags" else map(parse_inner_bag, inner_bag_str.split(", "))
        bag_rules.set_contains(container_bag, inner_bag_list)

    return bag_rules


def main():
    bag_rules = parse_graph(sys.stdin)
    holding_bags = bag_rules.find_num_inner_bags('shiny gold')
    print(holding_bags)

if __name__ == '__main__':
    main()
