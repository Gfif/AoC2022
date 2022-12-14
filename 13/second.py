# FILENAME = "13/example.txt"
FILENAME = "13/input.txt"
import functools

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


def bubblesort(elements):
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if compare(elements[i + 1], elements[i]):
                swapped = True
                # swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i]       
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return
            

def main():
    res = 0
    a = [[[2]], [[6]]]
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
            f, _ = parse(first[1:])
            s, _ = parse(second[1:])

            a.append(f)
            a.append(s)

    bubblesort(a)
    print(a)

    return (a.index([[2]]) + 1) * (a.index([[6]]) + 1)


if __name__ == "__main__":
    r = main()
    print(r)
