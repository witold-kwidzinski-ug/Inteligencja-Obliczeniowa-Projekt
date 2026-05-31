import math
import time
from collections import deque

colors = {
    1: "red",
    2: "orange",
    3: "yellow",
    4: "green",
    5: "blue",
    6: "cyan",
    7: "pink",
    8: "purple",
    9: "brown",
    10: "grey"
}
DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def can_reach(s, start, end):
    queue = deque([start])
    visited = {start}

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            return True

        for dir in DIRECTIONS:
            next = (x + dir[0], y + dir[1])

            if next[0] < 0 or next[0] >= len(s[0]):
                continue

            if next[1] < 0 or next[1] >= len(s):
                continue

            if next in visited:
                continue

            if s[next[1]][next[0]] == 0 or next == end:
                visited.add(next)
                queue.append(next)

    return False


def dfs_alg(s, cur, color, p, vals):
    c = list(p.keys())[color]

    if cur == p[c][1]:
        if color + 1 == len(p):
            return True

        return dfs_alg(s, p[list(p.keys())[color+1]][0], color + 1, p, vals)


    if cur != p[c][0]:
        s[cur[1]][cur[0]] = c

        if not can_reach(s, cur, p[c][1]):
            s[cur[1]][cur[0]] = 0
            return False

        for i in range(color+1, len(vals)):
            if not can_reach(s, vals[i][0], vals[i][1]):
                s[cur[1]][cur[0]] = 0
                return False

    dirs = DIRECTIONS[:]
    dirs.sort(key=lambda d: abs(cur[0] + d[0] - p[c][1][0]) + abs(cur[1] + d[1] - p[c][1][1]))

    for dir in dirs:
        next_step = (cur[0] + dir[0], cur[1] + dir[1])
        if next_step[0] < 0 or next_step[0] >= len(s[0]) or next_step[1] < 0 or next_step[1] >= len(s):
            continue

        if next_step == p[c][1] or s[next_step[1]][next_step[0]] == 0:
            if dfs_alg(s, next_step, color, p, vals):
                return True
    else:
        if (cur[0], cur[1]) != p[c][0] and (cur[0], cur[1]) != p[c][1]:
            s[cur[1]][cur[0]] = 0
        return False


def count_obstacles(s, point):
    amount = 0

    if point[0] - 1 < 0 or s[point[1]][point[0]-1] != 0:
        amount += 1
    if point[0] + 1 >= len(s[0]) or s[point[1]][point[0]+1] != 0:
        amount += 1
    if point[1] - 1 < 0 or s[point[1]-1][point[0]] != 0:
        amount += 1
    if point[1] + 1 >= len(s) or s[point[1]+1][point[0]] != 0:
        amount += 1

    return amount



def dfs(size, p):
    s = [[0 for _ in range(size)] for _ in range(size)]
    for i in list(p.keys()):
        for j in range(2):
            point = p[i][j]
            s[point[1]][point[0]] = i

    sorted_p = dict(sorted(p.items(), key=lambda s: math.dist(s[1][0], s[1][1])))

    for col in sorted_p:
        sorted_p[col].sort(key=lambda point: count_obstacles(s, point), reverse=True)

    vals = list(sorted_p.values())

    if dfs_alg(s, sorted_p[list(sorted_p.keys())[0]][0], 0, sorted_p, vals):
        return s
    return False