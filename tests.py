import time

from dfs import dfs
from ga import ga
from bfs import bfs
from sa import sa
from maze_generator import maze_generator

dfs_times = {}
ga_times = {}
bfs_times = {}
sa_times = {}

for i in [5, 6, 7]:
    dfs_times[f"{i}x{i}"] = []
    ga_times[f"{i}x{i}"] = []
    bfs_times[f"{i}x{i}"] = []
    sa_times[f"{i}x{i}"] = []
    for j in range(5):
        maze_points = maze_generator(i, i)
        print(f"Maze found {j+1}/5")
        solution = dfs(i, maze_points)

        print(f"Starting dfs")
        start = time.time()
        result = dfs(i, maze_points)
        end = time.time()
        if result != solution:
            dfs_times[f"{i}x{i}"].append(None)
        else:
            dfs_times[f"{i}x{i}"].append(end - start)

        print(f"Starting ga")
        start = time.time()
        result = ga(i, maze_points)
        end = time.time()
        if result != solution:
            ga_times[f"{i}x{i}"].append(None)
        else:
            ga_times[f"{i}x{i}"].append(end - start)

        print(f"Starting bfs")
        start = time.time()
        result = bfs(i, maze_points)
        end = time.time()
        if result != solution:
            bfs_times[f"{i}x{i}"].append(None)
        else:
            bfs_times[f"{i}x{i}"].append(end - start)

        print(f"Starting sa")
        start = time.time()
        result = sa(i, maze_points)
        end = time.time()
        if result != solution:
            sa_times[f"{i}x{i}"].append(None)
        else:
            sa_times[f"{i}x{i}"].append(end - start)


for i in [5, 6, 7]:
    print(f"======={i}x{i}=======")

    valid_times = 0
    correct_puzzles = 0

    for t in list(dfs_times[f"{i}x{i}"]):
        if t is not None:
            valid_times += t
            correct_puzzles += 1

    print(f"dfs: {valid_times/5}s, {correct_puzzles}/5")
#####################################################################
    valid_times = 0
    correct_puzzles = 0

    for t in list(ga_times[f"{i}x{i}"]):
        if t is not None:
            valid_times += t
            correct_puzzles += 1

    print(f"ga: {valid_times / 5}s, {correct_puzzles}/5")
#####################################################################
    valid_times = 0
    correct_puzzles = 0

    for t in list(bfs_times[f"{i}x{i}"]):
        if t is not None:
            valid_times += t
            correct_puzzles += 1

    print(f"bfs: {valid_times / 5}s, {correct_puzzles}/5")
#####################################################################
    valid_times = 0
    correct_puzzles = 0

    for t in list(sa_times[f"{i}x{i}"]):
        if t is not None:
            valid_times += t
            correct_puzzles += 1

    print(f"sa: {valid_times / 5}s, {correct_puzzles}/5")

