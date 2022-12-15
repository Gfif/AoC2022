import re
from collections import namedtuple

Boundary = namedtuple("Boundary", ["begin", "end"])


FILENAME = "15/example.txt"
TARGET = 10
X, Y = Boundary(-30, 30), Boundary(0, 26)

FILENAME = "15/input.txt"
TARGET = 2_000_000
X, Y = Boundary(-1_000_000, 4_500_000), Boundary(2_000_000, 2_000_000)



class Solution():
    def __init__(self):
        self.pairs = self.parse_pairs()

    @staticmethod
    def distance(coord1, coord2):
        return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
    
    @staticmethod
    def merge_ranges(ranges):
        res = []
        for begin, end in sorted(ranges):
            if res and res[-1][1] >= begin - 1:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([begin, end])
        return res

    def parse_pairs(self):
        pairs = []
        with open(FILENAME, "r") as f:
            for line in f:
                line = line.strip()
                coords = re.findall(r"x=(-?\d+), y=(-?\d+)", line)
                sensor, beacon = list((int(x), int(y)) for x, y in coords)
                pairs.append((sensor, beacon))
        return pairs

    def solve(self):
        self.parse_pairs()
        
        res = 0
        for x in range(X.begin, X.end):
            for sensor, beacon in self.pairs:
                point = [x, TARGET]
                if self.distance(sensor, point) <= self.distance(sensor, beacon):
                    res += 1
                    break

        return res - 1


if __name__ == "__main__":
    solution = Solution().solve()
    print(solution)
