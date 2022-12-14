import time
from copy import deepcopy

N = 26
FILENAME = "9/example.txt"
start = [5, 11]


def pprint(visited_map, head=None, tails=None):
    mmap = deepcopy(visited_map)
    if tails:
        set_tail(mmap, tails[0], 1)
        for i, tail in enumerate(tails[1:], 2):
            if tail == tails[i - 2]:
                continue
            set_tail(mmap, tail, i)
    if head:
        set_head(mmap, head)
    for raw in reversed(mmap):
        print(" ".join(str(c) for c in raw))
    print("_______")
    time.sleep(0.1)


def set_head(mmap, coord):
    mmap[coord[0]][coord[1]] = "H"


def set_tail(mmap, coord, num):
    mmap[coord[0]][coord[1]] = str(num)


def mark_visited(visited_map, coord):
    visited_map[coord[0]][coord[1]] = "#"


def get_diff(head, tail):
    return [abs(head[0] - tail[0]), abs(head[1] - tail[1])]


def is_need_to_move_tail(head, tail):
    dff = get_diff(head, tail)
    return dff[0] > 1 or dff[1] > 1


def apply_delta(base, delta):
    return [base[0] + delta[0], base[1] + delta[1]]


def get_delta(direction):
    if direction == "R":
        delta = [0, 1]
    elif direction == "U":
        delta = [1, 0]
    elif direction == "L":
        delta = [0, -1]
    elif direction == "D":
        delta = [-1, 0]
    else:
        raise Exception("LOL")

    return delta


def main():
    f = open(FILENAME)
    visited_map = [["." for _ in range(N)] for _ in range(N)]
    head = deepcopy(start)
    tails = [deepcopy(start) for _ in range(1, 10)]
    mark_visited(visited_map, tails[-1])  
    pprint(visited_map, head, tails)
    time.sleep(5)

    for line in f:
        direction, count = line.split()
        count = int(count)

        delta = get_delta(direction)

        for _ in range(count):
            head = apply_delta(head, delta)

            prev_tail = head
            for i, tail in enumerate(tails):
                if is_need_to_move_tail(prev_tail, tail):
                    tail_delta = [0, 0]
                    if prev_tail[1] != tail[1]:
                        tail_delta[1] = 1 if prev_tail[1] > tail[1] else -1
                    if prev_tail[0] != tail[0]:
                        tail_delta[0] = 1 if prev_tail[0] > tail[0] else -1
                    tail = apply_delta(tail, tail_delta)
                    tails[i] = apply_delta(tails[i], tail_delta)

                prev_tail = tail

            mark_visited(visited_map, tails[-1])
            pprint(visited_map, head, tails)
        
        pprint(visited_map)

    return sum(visited_map[i][j]=="#" for i in range(N) for j in range(N))


if __name__ == "__main__":
    res = main()
    # print(res)
