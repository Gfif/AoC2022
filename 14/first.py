import time
import sys


class Solution:
    FILENAME = "14/input.txt"
    N, M = 100000, 200

    def __init__(self):
        self.map = [[0] * self.M for _ in range(self.N)]
        self.max_y = 0
        self.min_y = self.M
        self.max_x = 0
        self.min_x = self.N

    def update_minmax(self, x, y):
        self.max_x = max(self.max_x, x)
        self.min_x = min(self.min_x, x)
        self.max_y = max(self.max_y, y)
        self.min_y = min(self.min_y, y)

    def print_map(self):
        time.sleep(0.1)
        lines = []
        c = {0: ".", 1: "#", 2: "o"}
        for row in self.map[self.min_x - 30 :self.max_x + 30]:
            lines.append("".join(c[x] for x in row[self.min_y - 10: self.max_y + 10]))
        
        sys.stdout.write("\n".join(lines) + "\n")
        sys.stdout.flush()

    def fill_rocks(self, points):
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    self.map[x1][y] = 1

            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    self.map[x][y1] = 1

            else:
                raise Exception("Invalid points: %s, %s" % (points[i], points[i + 1]))

            self.update_minmax(x1, y1)
            self.update_minmax(x2, y2)

    def fill_floor(self):
        for i in range(self.N):
            self.map[i][self.max_y + 2] = 1

    def next_step(self, point):
        x, y = point
        if self.map[x][y + 1] == 0:
            return [x, y + 1]

        if self.map[x - 1][y + 1] == 0:
            return [x - 1, y + 1]

        if self.map[x + 1][y + 1] == 0:
            return [x + 1, y + 1]

        return point

    def simulate_fall(self):
        prev = None
        curr = [500, 0]

        while True:
            while prev != curr:
                prev = curr
                try:
                    curr = self.next_step(curr)
                    if curr == [500, 0]:
                        self.map[curr[0]][curr[1]] = 2
                        return
                except IndexError:
                    return

            self.map[curr[0]][curr[1]] = 2
            self.print_map()
            prev = None
            curr = [500, 0]
    
    def main(self):
        with open(self.FILENAME) as f:
            for line in f:
                line = line.strip()
                parts = line.split(" -> ")
                points = [tuple(map(int, part.split(","))) for part in parts]
                
                self.fill_rocks(points)
            
            self.fill_floor()
            self.print_map()
            self.simulate_fall()

            print(sum(sum(1 for x in row if x == 2) for row in self.map))



if __name__ == "__main__":
    Solution().main()
