# FILENAME = "13/example.txt"
FILENAME = "13/input.txt"


def find_end(line: str) -> int:
    return len(line) - "".join(reversed(line)).index("]") - 1


def parse(s):
    res = []
    val = None

    i = 0
    while i < len(s):
        c = s[i]

        if c == "[":
            vals, size = parse(s[i+1:])
            res.append(vals)
            i += size
        elif c == "]":
            if val is not None:
                res.append(val)
            return res, i + 3
        elif c.isdigit():
            if val is None:
                val = 0
            val = val * 10 + int(c)
            i += 1
        elif c == ",":
            if val is not None:
                res.append(val)
            val = None
            i += 1
        
    return res, i + 1

# def parse_line(line) -> list:
    res = []
    stack = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == "[":
            j = find_end(line[i:])
            res.append(parse_line(line[i + 1: i + j]))
            i += j + 1

        elif c == "]":
            i += 1
            continue

        else:
            next_open_breaket = line[i:].find("[")
            next_close_breaket = line[i:].find("]")
            next_breaket = min(next_open_breaket, next_close_breaket)

            if next_breaket == -1:
                res.extend([int(c) for c in line[i:].split(",")])
                return res
            else:
                res.extend([int(c) for c in line[i: i + next_breaket].split(",")])
                i += next_breaket

            return res



    return res
                

def compare(f, s) -> bool:

    m = min(len(f), len(s))

    for i in range(m):
        if isinstance(f[i], int) and isinstance(s[i], int):
            if f[i] < s[i]:
                return True
            elif f[i] > s[i]:
                return False
            else:
                continue
        elif isinstance(f[i], list) and isinstance(s[i], list):
            res = compare(f[i], s[i])
            if res is not None:
                return res
            else:
                continue
        elif isinstance(f[i], int):
            res = compare([f[i]], s[i])
            if res is not None:
                return res
            else:
                continue
        elif isinstance(s[i], int):
            res = compare(f[i], [s[i]])
            if res is not None:
                return res
            else:
                continue
        else:
            raise Exception("Lol")
            
    if m < len(s):
        return True
    elif m < len(f):
        return False
    elif len(s) == len(f):
        return None
    else:
        raise Exception("Lol2")

def main():
    res = 0
    with open(FILENAME) as f:
        first = second = ""
        i = 0
        for line in f:
            line = line.strip()
            if not line:
                first = second = ""
                continue

            if not first:
                first = line
                continue

            if not second:
                second = line

            i += 1
            print(first, second)
            f, _ = parse(first[1:])
            print(f)
            s, _ = parse(second[1:])
            print(s)

            com = compare(f, s)
            print(com)

            if com:
                res += i

        return res


if __name__ == "__main__":
    r = main()
    print(r)