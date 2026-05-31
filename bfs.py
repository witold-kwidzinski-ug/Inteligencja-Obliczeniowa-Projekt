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


def serialize(board):
    return tuple(tuple(row) for row in board)


def bfs(size, p):
    s = [[0 for _ in range(size)] for _ in range(size)]
    for i in list(p.keys()):
        for j in range(2):
            point = p[i][j]
            s[point[1]][point[0]] = i

    colors = list(p.keys())

    queue = deque()
    queue.append((s, p[colors[0]][0], 0))

    visited_states = set()

    while queue:
        board, cur, c = queue.popleft()

        state = (serialize(board), cur, c)
        if state in visited_states:
            continue
        visited_states.add(state)

        color = colors[c]

        if cur == p[color][1]:

            if c + 1 == len(colors):
                return board

            queue.append(
                (
                    board,
                    p[colors[c+1]][0],
                    c+1
                )
            )

            continue

        dirs = DIRECTIONS[:]

        for dir in dirs:
            next_step = (cur[0] + dir[0], cur[1] + dir[1])

            if next_step[0] < 0 or next_step[0] >= len(board[0]):
                continue

            if next_step[1] < 0 or next_step[1] >= len(board):
                continue

            if next_step == p[color][1] or board[next_step[1]][next_step[0]] == 0:
                tmp_board = [row[:] for row in board]

                if next_step != p[color][1]:
                    tmp_board[next_step[1]][next_step[0]] = color


                queue.append(
                    (
                        tmp_board,
                        next_step,
                        c
                    )

                )


#
# points = {
#     1: [(0,0), (1, 4)],
#     2: [(3,4), (4, 1)],
#     3: [(3,3), (4, 0)],
#     4: [(1,3), (2, 0)],
#     5: [(2,1), (2, 4)],
# }
#
# print(bfs(5, points))
#
