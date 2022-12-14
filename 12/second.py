from copy import deepcopy
import time
import queue

# FILENAME = "12/example.txt"
# START_POSITION = [0, 0]
# END_POSITION = [2, 5]
# POSITION = START_POSITION

FILENAME = "12/input.txt"
START_POSITION = [20, 0]
END_POSITION = [20, 55]
POSITION = START_POSITION



def pprint(inp, visited):
    res = deepcopy(inp)
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if visited[i][j]:
                res[i][j] = "."

    print("\n".join("".join(l) for l in res))

    print("------")


def get_value(inp, position):
    if inp[position[0]][position[1]] == "S":
        return "a"
    if inp[position[0]][position[1]] == "E":
        return "z"

    return inp[position[0]][position[1]]


def can_step(inp, position, new_position):
    new_val = get_value(inp, new_position)
    val = get_value(inp, position)

    if ord(new_val) <= ord(val) + 1:
        return True

    return False


def get_lowest_path(inp, visited, position, depth=1):
    # pprint(inp, visited)
    # time.sleep(1 / 30)
    # if inp[position[0]][position[1]] == "E":
    #     return 0

    # visited[position[0]][position[1]] = depth
    # pathes = []
    # if position[0] > 0 and not visited[position[0] - 1][position[1]] and can_step(inp, position, [position[0] - 1, position[1]]):
    #     pathes.append(get_lowest_path(inp, visited,[position[0] - 1, position[1]], depth=depth + 1))
    # if position[0] < len(inp) - 1 and not visited[position[0] + 1][position[1]] and can_step(inp, position, [position[0] + 1, position[1]]):
    #     pathes.append(get_lowest_path(inp, visited, [position[0] + 1, position[1]], depth=depth + 1))
    # if position[1] > 0 and not visited[position[0]][position[1] - 1] and can_step(inp, position, [position[0], position[1] - 1]):
    #     pathes.append(get_lowest_path(inp, visited, [position[0], position[1] - 1], depth=depth + 1))
    # if position[1] < len(inp[0]) - 1 and not visited[position[0]][position[1] + 1] and can_step(inp, position, [position[0], position[1] + 1]):
    #     pathes.append(get_lowest_path(inp, visited, [position[0], position[1] + 1], depth=depth + 1))

    # return min(pathes) + 1 if pathes else float("inf")

    q = queue.Queue()
    q.put((position, 0))
    visited[position[0]][position[1]] = 1
    pprint(inp, visited)
    time.sleep(10)

    while not q.empty():

        position, depth = q.get()

        # print(position, depth)
        pprint(inp, visited)
    
        next_positions = [
            [position[0] - 1, position[1]],
            [position[0] + 1, position[1]],
            [position[0], position[1] - 1],
            [position[0], position[1] + 1],
        ]

        for np in next_positions:
            if np[0] < 0 or np[0] >= len(inp):
                continue
            if np[1] < 0 or np[1] >= len(inp[0]):
                continue

            if can_step(inp, position, np) and not visited[np[0]][np[1]]:
                if np == END_POSITION:
                    return depth + 1
                # print(f"Adding {np, depth+1} to queue")
                q.put((np, depth + 1))
                visited[np[0]][np[1]] = 1

        
        

def main():
    inp = []

    with open(FILENAME) as f:
        for line in f:
            line = line.strip()
            inp.append([l for l in line])

    visited = [[0 for _ in range(len(inp[0]))] for _ in range(len(inp))]

    position = POSITION
    if inp[position[0]][position[1]] != "S":
        raise Exception("Wrong position")
    
    visited[position[0]][position[1]] = 1
    get_lowest_path(inp, visited, position)


if __name__ == "__main__":
    main()
