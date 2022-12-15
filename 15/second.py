import re
from collections import namedtuple

Boundary = namedtuple("Boundary", ["begin", "end"])

FILENAME = "15/example.txt"
X, Y = Boundary(0, 20), Boundary(0, 20)

FILENAME = "15/input.txt"
X, Y = Boundary(0, 4_000_000), Boundary(0, 4_000_000)


class Solution():
    def __init__(self):
        self.pairs = self.parse_pairs()

    @staticmethod
    def tuning_frequency(point):
        return point[0] * 4000000 + point[1]

    @staticmethod
    def distance(point1, point2):
        return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])

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

    def get_empty_ranges(self, x):
        empty_ranges = []
        for sensor, beacon in self.pairs:
            dist_to_sensor_by_x = abs(sensor[0] - x)
            empty_dist_by_y = self.distance(sensor, beacon) - dist_to_sensor_by_x
            if empty_dist_by_y > 0:
                empty_ranges.append((sensor[1] - empty_dist_by_y, sensor[1] + empty_dist_by_y))

        return self.merge_ranges(empty_ranges)

    def solve(self):        
        for x in range(X.begin, X.end):
            ranges = self.get_empty_ranges(x)

            assert len(ranges) in (1, 2), f"len(ranges) = {len(ranges)}"

            if len(ranges) == 1:
                continue

            assert ranges[0][1] + 1 == ranges[1][0] - 1, (
                f"More than one allowed points in x = {x}"
            )

            y = ranges[0][1] + 1
            point = [x, y]
            print(point)

            return self.tuning_frequency(point)

        return 0


if __name__ == "__main__":
    solution = Solution().solve()
    print(solution)
