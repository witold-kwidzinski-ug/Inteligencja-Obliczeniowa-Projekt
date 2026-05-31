import math
import random
from dfs import dfs

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



def maze_generator(size, color_amount):
    maze = [[0 for _ in range(size)] for _ in range(size)]

    while True:
        used_points = {}
        for i in range(color_amount):
            used_points[i+1] = []
            valid = False
            while not valid:
                start = (random.randint(0, size-1), random.randint(0, size-1))
                end = (random.randint(0, size-1), random.randint(0, size-1))
                for color in used_points:
                    if start == end or math.dist(start, end) == 1 or start in used_points[color] or end in used_points[color]:
                        break
                else:
                    maze[start[1]][start[0]] = i + 1
                    maze[end[1]][end[0]] = i + 1
                    used_points[i+1].append(start)
                    used_points[i+1].append(end)
                    valid = True
        board = dfs(size, used_points)
        if board:
            unused_points = []
            for i in range(size):
                for j in range(size):
                    if board[i][j] == 0:
                        unused_points.append((j, i))

            return used_points, unused_points