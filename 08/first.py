
def main():
    with open("8/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        mmap = [[int(m) for m in line] for line in lines]
        print(mmap)
        size = len(mmap)

        vizible_map = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            vizible_map[i][0] = 1
            vizible_map[0][i] = 1
            vizible_map[i][size - 1] = 1
            vizible_map[size - 1][i] = 1

        for i in range(1, size - 1):
            for j in range(1, size - 1):
                prev_trees = []
                prev_trees.append([mmap[x][j] for x in range(i)])
                prev_trees.append([mmap[i][x] for x in range(j)])
                prev_trees.append([mmap[x][j] for x in range(i + 1, size)])
                prev_trees.append([mmap[i][x] for x in range(j + 1, size)])
            
                if any(mmap[i][j] > max(pt) for pt in prev_trees):
                    vizible_map[i][j] = 1

        print(mmap)
        print(vizible_map)

        return sum(vizible_map[i][j] for i in range(size) for j in range(size))


if __name__ == "__main__":
    print(main())