from queue import Queue
from dataclasses import dataclass


FILENAME = "11/input.txt"
NUM = 4


@dataclass
class MonkeyConfig:
    items: Queue
    operation: str
    test: int
    if_true: int
    if_false: int
    counter: int = 0

    @classmethod
    def new(cls, items):
        return cls(items, None, None, None, None)


def get_starting_items(line):
    items = line.split(":")[1].strip()
    items = items.split(",")
    items = [int(item) for item in items]
    q = Queue()
    for item in items:
        q.put(item)
    return q


def get_operation(line):
    return line.split("=")[1].strip()


def get_test(line):
    return int(line.split(" ")[-1].strip())


def get_if_true(line):
    return int(line.split(" ")[-1].strip())


def get_if_false(line):
    return int(line.split(" ")[-1].strip())


def get_configs():
    with open(FILENAME) as f:
        configs = []

        for line in f:
            line = line.strip()

            if not line:
                configs.append(cfg)
            elif line.startswith("Monkey"):
                pass
            elif line.startswith("Starting items"):
                items = get_starting_items(line)
                cfg = MonkeyConfig.new(items)
            elif line.startswith("Operation"):
                cfg.operation = get_operation(line)
            elif line.startswith("Test"):
                cfg.test = get_test(line)
            elif line.startswith("If true"):
                cfg.if_true = get_if_true(line)
            elif line.startswith("If false"):
                cfg.if_false = get_if_false(line)
            else:
                raise ValueError("Unknown line: {}".format(line))
        
        configs.append(cfg)
        return configs


def run_round(configs):
    
    for cfg in configs:
        while not cfg.items.empty():
            item = cfg.items.get()
            cfg.counter += 1
            operation = cfg.operation.replace("old", str(item))
            new = eval(operation)

            new = new // 3

            if not new % cfg.test:
                configs[cfg.if_true].items.put(new)
            else:
                configs[cfg.if_false].items.put(new)


def print_items(configs):
    for cfg in configs:
        res = ""
        for item in cfg.items.queue:
            res += str(item) + ", "
        print(res[:-2])

def main():
    configs = get_configs()

    for _ in range(20):
        run_round(configs)
    print_items(configs)

    counters = [cfg.counter for cfg in configs]
    print(counters)

    counters.sort(key=lambda x: -x)

    return counters[0] * counters[1]
    

if __name__ == '__main__':
    print(main())
