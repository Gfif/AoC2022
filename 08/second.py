
def main():
    with open("8/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        mmap = [[int(m) for m in line] for line in lines]
        print(mmap)
        size = len(mmap)

        vizible_map = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(0, size):
            for j in range(0, size):
                prev_trees = []
                prev_trees.append(list(reversed([mmap[x][j] for x in range(i)])))
                prev_trees.append(list(reversed([mmap[i][x] for x in range(j)])))
                prev_trees.append([mmap[x][j] for x in range(i + 1, size)])
                prev_trees.append([mmap[i][x] for x in range(j + 1, size)])

                print(i, j, mmap[i][j])
                print(prev_trees)
            
                scores = []
                for pt in prev_trees:
                    score = 0
                    for p in pt:
                        if p >= mmap[i][j]:
                            score += 1
                            break
                        else:
                            score += 1
                    scores.append(score)

                print(scores)
                vizible_map[i][j] = scores[0] * scores[1] * scores[2] * scores[3]
                print(vizible_map[i][j])


        print(mmap)
        print(vizible_map)

        return max(vizible_map[i][j] for i in range(size) for j in range(size))


if __name__ == "__main__":
    print(main())