import math
import time

stage = [
    [1, 0, 4, 0, 3],
    [0, 0, 5, 0, 2],
    [0, 0, 0, 0, 0],
    [0, 4, 0, 3, 0],
    [0, 1, 5, 2, 0]
]

colors = {
    1: "red",
    2: "orange",
    3: "yellow",
    4: "green",
    5: "blue",
}

points = {
    1: [(0,0), (1, 4)],
    2: [(3,4), (4, 1)],
    3: [(3,3), (4, 0)],
    4: [(1,3), (2, 0)],
    5: [(2,1), (2, 4)],
}

def print_puzzle(s):
    for row in s:
        print(row)
    print()

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def dfs(s, cur, color):


    if cur != points[color][0]:
        s[cur[1]][cur[0]] = color

    if cur == points[color][1]:
        if color + 1 == len(points) + 1:
            return True

        return dfs(s, points[color + 1][0], color + 1)

    dirs = DIRECTIONS[:]
    dirs.sort(key=lambda d: math.dist((cur[0] + d[0], cur[1] + d[1]), points[color][1]))

    for dir in dirs:
        next_step = (cur[0] + dir[0], cur[1] + dir[1])
        if next_step[0] < 0 or next_step[0] >= len(s[0]) or next_step[1] < 0 or next_step[1] >= len(s):
            continue

        if next_step == points[color][1] or s[next_step[1]][next_step[0]] == 0:
            if dfs(s, next_step, color):
                return True
    else:
        if (cur[0], cur[1]) != points[color][0] and (cur[0], cur[1]) != points[color][1]:
            s[cur[1]][cur[0]] = 0
        return False



start = time.time()

dfs(stage, points[1][0], 1)

stop = time.time()

print_puzzle(stage)

print(stop-start)
