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

    def fitness_func(model, solution, solution_idx):
        tmp = [row[:] for row in s]
        color = 1
        cur = p[color][0]

        collisions = 0

        for step in solution:
            next_step = (cur[0] + DIRECTIONS[step][0], cur[1] + DIRECTIONS[step][1])
            if len(tmp[0]) > next_step[0] >= 0 and 0 <= next_step[1] < len(tmp):
                if tmp[next_step[1]][next_step[0]] == 0 or next_step == p[color][1]:
                    cur = next_step
                    if cur == p[color][1]:
                        color += 1
                        if color > len(c):
                            return 1000000
                        cur = p[color][0]
                    else:
                        tmp[cur[1]][cur[0]] = color
                else:
                    collisions += 1

        return color * 100 - collisions*20 - math.dist(p[color][1], cur)

    sol_per_pop = 50
    num_genes = len(s) * len(s[0]) - len(p)*2

    num_parents_mating = 5
    num_generations = 1000
    keep_parents = 2

    parent_selection_type = "sss"

    crossover_type = "single_point"

    mutation_type = "random"
    mutation_percent_genes = 8

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
                           mutation_percent_genes=mutation_percent_genes,
                           stop_criteria=["reach_1000000"])

    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print(solution)
    print(solution_fitness)


ga(stage, colors, points)