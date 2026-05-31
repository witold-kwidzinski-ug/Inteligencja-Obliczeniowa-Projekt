import math
import random

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

def evaluate(solution, size, p):
    board = [[0 for _ in range(size)] for _ in range(size)]

    final_score = 0

    colors = list(p.keys())

    for i in range(len(solution)):
        moves = solution[i]
        cur = p[colors[i]][0]

        for step in moves:
            next_step = (cur[0] + DIRECTIONS[step][0], cur[1] + DIRECTIONS[step][1])
            if len(board[0]) > next_step[0] >= 0 and 0 <= next_step[1] < len(board):
                if board[next_step[1]][next_step[0]] == 0 or next_step == p[colors[i]][1]:

                    cur = next_step

                    if cur == p[colors[i]][1]:
                        final_score += 50000
                        continue
                    else:
                        board[cur[1]][cur[0]] = colors[i]
                else:
                    final_score -= 100
        final_score -= abs(cur[0] - p[colors[i]][1][0]) + abs(cur[1] - p[colors[i]][1][1])

    return final_score

def mutate(sol):
    tmp = [row[:] for row in sol]

    tmp[random.randint(0, len(tmp)-1)][random.randint(0, len(tmp[0])-1)] = random.randint(0,3)

    return tmp


def sa_alg(size, p):
    solution = [[random.randint(0, 3) for _ in range(size * size)] for _ in range(len(p))]


    temp = 100.0
    cooling = 0.995

    best = solution
    best_score = evaluate(solution, size, p)

    current = solution
    current_score = best_score


    for _ in range(5000):
        new_solution = mutate(current)

        new_score = evaluate(new_solution, size, p)

        delta = new_score - current_score

        if delta > 0 or random.random() < math.exp(delta / temp):
            current = new_solution
            current_score = new_score

            if new_score > best_score:
                best = new_solution
                best_score = new_score

        temp *= cooling

        if temp <= 0.1:
            break

    return best

def sa(size, p):
    solution = sa_alg(size, p)

    board = [[0 for _ in range(size)] for _ in range(size)]

    for color, points in p.items():
        for point in points:
            board[point[1]][point[0]] = color

    colors = list(p.keys())

    for i in range(len(solution)):
        moves = solution[i]
        cur = p[colors[i]][0]

        for step in moves:
            next_step = (cur[0] + DIRECTIONS[step][0], cur[1] + DIRECTIONS[step][1])
            if len(board[0]) > next_step[0] >= 0 and 0 <= next_step[1] < len(board):
                if board[next_step[1]][next_step[0]] == 0 or next_step == p[colors[i]][1]:

                    cur = next_step

                    if cur == p[colors[i]][1]:
                        continue
                    else:
                        board[cur[1]][cur[0]] = colors[i]

    return board
