import math

import pygad

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

def ga(s, c, p):
    DIRECTIONS = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)} # right,down,left,up
    gene_space = [0, 1, 2, 3]
    MOVES_PER_COLOR = len(s) * len(s[0]) - len(c)*2

    def fitness_func(model, solution, solution_idx):
        tmp = [row[:] for row in s]

        collisions = 0

        final_score = 0

        for col in range(len(c)):
            cur = p[col+1][0]
            moves = solution[MOVES_PER_COLOR*col:MOVES_PER_COLOR*(col+1)]
            for step in moves:
                next_step = (cur[0] + DIRECTIONS[step][0], cur[1] + DIRECTIONS[step][1])
                if len(tmp[0]) > next_step[0] >= 0 and 0 <= next_step[1] < len(tmp):
                    if tmp[next_step[1]][next_step[0]] == 0 or next_step == p[col+1][1]:
                        old_dist = math.dist(cur, p[col+1][1])
                        new_dist = math.dist(next_step, p[col+1][1])

                        if new_dist < old_dist:
                            final_score += 5
                        else:
                            final_score -= 2

                        cur = next_step
                        if cur == p[col+1][1]:
                            final_score += 10000
                            break
                        else:
                            tmp[cur[1]][cur[0]] = col+1
                    else:
                        collisions += 1
                else:
                    collisions += 1
            else:
                final_score -= math.dist(cur, p[col+1][1])

        for row in tmp:
            final_score -= row.count(0) * 10

        return final_score - collisions * 20

    sol_per_pop = 100
    num_genes = MOVES_PER_COLOR * len(c)


    num_parents_mating = 5
    num_generations = 1000
    keep_parents = 2

    parent_selection_type = "sss"

    crossover_type = "single_point"

    mutation_type = "random"
    mutation_percent_genes = 5

    ga_instance = pygad.GA(gene_space=gene_space,
                           num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_func,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes)

    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()

    for col in range(len(c)):
        moves = solution[MOVES_PER_COLOR * col:MOVES_PER_COLOR * (col + 1)]
        cur = p[col+1][0]
        for step in moves:
            next_step = (cur[0] + DIRECTIONS[step][0], cur[1] + DIRECTIONS[step][1])
            if len(s[0]) > next_step[0] >= 0 and 0 <= next_step[1] < len(s):
                if s[next_step[1]][next_step[0]] == 0 or next_step == p[col + 1][1]:
                    cur = next_step
                    if cur == points[col+1][1]:
                        break
                    s[cur[1]][cur[0]] = col+1


ga(stage, colors, points)

for row in stage:
    print(row)