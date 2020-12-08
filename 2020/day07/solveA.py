""" Super hacky code, written to get an answer fast"""

from collections import defaultdict
import sys


class BagRules:
    """Ignores numbers since I don't think they're needed for part 1?"""
    def __init__(self):
        self.contained_by = defaultdict(set)  # key is contained by value

    def contains(self, a, b_list):
        """a bags contain X b1 bags, Y b2 bags, Z b3 bags"""
        for b in b_list:
            self.contained_by[b].add(a)

    def find_bags_that_can_hold(self, color):
        to_ret = set(self.contained_by[color])
        for c in self.contained_by[color]:
            to_ret.update(self.find_bags_that_can_hold(c))

        return to_ret

def parse_bag(bag_string):
    """ Drop 'bag' or 'bags'"""
    return bag_string.rstrip().rsplit(' ', 1)[0]

def parse_inner_bag(inner_bag_string):
    """ Drop number and 'bag' or 'bags'"""
    return " ".join(inner_bag_string.split()[1:-1])

def parse_graph(stream):
    bag_rules = BagRules()
    for line in stream:
        line = line.rstrip().rstrip(".")
        container_bag_str, inner_bag_str = line.split(" contain ")
        container_bag = parse_bag(container_bag_str)
        inner_bag_list = [] if inner_bag_str == "no other bags" else map(parse_inner_bag, inner_bag_str.split(", "))
        bag_rules.contains(container_bag, inner_bag_list)

    return bag_rules


def main():
    bag_rules = parse_graph(sys.stdin)
    holding_bags = bag_rules.find_bags_that_can_hold('shiny gold')
    print(len(holding_bags))

if __name__ == '__main__':
    main()
