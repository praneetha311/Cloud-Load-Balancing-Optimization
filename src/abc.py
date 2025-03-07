# abc.py

import numpy as np

class ArtificialBeeColony:
    def __init__(self, cloud_sim, num_bees, num_iterations, limit=20):
        self.cloud_sim = cloud_sim
        self.num_bees = num_bees
        self.num_iterations = num_iterations
        self.limit = limit
        self.solutions = [self.generate_random_solution() for _ in range(num_bees)]
        self.fitness = [self.calculate_fitness(sol) for sol in self.solutions]
        self.trials = [0] * num_bees

    def optimize(self):
        for _ in range(self.num_iterations):
            self.employed_bee_phase()
            self.onlooker_bee_phase()
            self.scout_bee_phase()

        best_index = np.argmax(self.fitness)
        return self.solutions[best_index]

    def generate_random_solution(self):
        return [(task, np.random.randint(self.cloud_sim.num_vms)) for task in range(self.cloud_sim.num_tasks)]

    def calculate_fitness(self, solution):
        makespan = self.cloud_sim.calculate_makespan(solution)
        return 1 / (1 + makespan)

    def employed_bee_phase(self):
        for i in range(self.num_bees):
            new_solution = self.generate_neighbor(self.solutions[i])
            new_fitness = self.calculate_fitness(new_solution)
            if new_fitness > self.fitness[i]:
                self.solutions[i] = new_solution
                self.fitness[i] = new_fitness
                self.