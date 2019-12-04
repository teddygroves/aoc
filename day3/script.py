from typing import Tuple, List


def get_input():
    with open('input.txt', 'r') as f:
        return f.readlines()


def get_manhattan_distance(point: Tuple[int]):
    return abs(point[0]) + abs(point[1])


def get_total_steps(crosspoint: Tuple[int]):
    return crosspoint[2] + crosspoint[3]


def update_points(points: List[int], direction: str, distance: int):
    current_x, current_y = points[-1]
    new_points = points.copy()
    if direction == 'R':
        for i in range(1, distance + 1):
            new_points.append((current_x + i, current_y))
    elif direction == 'L':
        for i in range(1, distance + 1):
            new_points.append((current_x - i, current_y))
    elif direction == 'U':
        for i in range(1, distance + 1):
            new_points.append((current_x, current_y + i))
    elif direction == 'D':
        for i in range(1, distance + 1):
            new_points.append((current_x, current_y - i))
    else:
        raise ValueError("Unknown direction: " + direction)
    return new_points
            

def get_points(movestring: str):
    moves = movestring.split(',')
    points = [(0, 0)]
    for move in moves:
        direction = move[0]
        distance = int(move[1:])
        points = update_points(points, direction, distance)
    return points


def get_crosspoints(points_a: List[Tuple[int]], points_b: List[Tuple[int]]):
    index_a = {k: i for i,k in enumerate(points_a)}
    index_b = {k: i for i,k in enumerate(points_b)}
    intersection = set(points_a).intersection(set(points_b))
    return [
        (*point, index_a[point], index_b[point])
        for point in intersection
    ]


def get_crosspoint_with_fewest_steps(crosspoints: List[Tuple[int]]):
    return sorted(crosspoints, key=get_total_steps)[1]  # not 0 as that is the origin


def get_closest_point(points: List[Tuple[int]]):
    return sorted(points, key=get_manhattan_distance)[1] # not 0 as that is the origin


def main():
    movestring_a, movestring_b = get_input()
    points_a = get_points(movestring_a)
    points_b = get_points(movestring_b)
    crosspoints = get_crosspoints(points_a, points_b)
    closest_crosspoint = get_closest_point(crosspoints)
    crosspoint_with_fewest_steps = get_crosspoint_with_fewest_steps(crosspoints)
    print("Closest crosspoint: " + str(closest_crosspoint))
    print("Closest crosspoint manhattan distance: "
          + str(get_manhattan_distance(closest_crosspoint)))
    print("Crosspoint with fewest steps: " + str(crosspoint_with_fewest_steps))
    print("Total steps to crosspoint with fewest steps: "
          + str(get_total_steps(crosspoint_with_fewest_steps)))

if __name__ == '__main__':
    main()
