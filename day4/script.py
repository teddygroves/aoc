import pandas as pd

LOW = 125730
HIGH = 579381


def expand_input(low, high):
    return list(map(lambda n: list(map(int, list(str(n)))), range(low, high)))


def check_criteria_part_1(l: list):
    return (
        any([l[i] == l[i+1] for i in range(len(l) - 1)])
        & all([l[i] >= l[i-1] for i in range(1, len(l))])
    )


def get_groups(l: list):
    g = []
    out = []
    for i, n in enumerate(l):
        if len(g) > 0 and n not in g:
            out.append(g)
            g = [n]
        else:
            g.append(n)
            if i == len(l) - 1:
                out.append(g)
    return out
            

def check_criteria_part_2(l: list):
    return (
        any([len(g) == 2 for g in get_groups(l)])
        & all([l[i] >= l[i-1] for i in range(1, len(l))])
    )

def main():
    expanded_input = expand_input(LOW, HIGH)
    criteria_satisfied_part_1 = map(check_criteria_part_1, expanded_input)
    criteria_satisfied_part_2 = map(check_criteria_part_2, expanded_input)
    print("Number of passwords satisfying part 1 criteria: "
          + str(sum(criteria_satisfied_part_1)))
    print("Number of passwords satisfying part 2 criteria: "
          + str(sum(criteria_satisfied_part_2)))

if __name__ == '__main__':
    main()
