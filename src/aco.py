# aco.py

import numpy as np

class AntColonyOptimization:
    def __init__(self, cloud_sim, num_ants, num_iterations, alpha=1, beta=2, evaporation_rate=0.5):
        self.cloud_sim = cloud_sim
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.pheromone = np.ones((cloud_sim.num_tasks, cloud_sim.num_vms))

    def optimize(self):
        best_solution = None
        best_makespan = float('inf')

        for _ in range(self.num_iterations):
            solutions = []
            for _ in range(self.num_ants):
                solution = self.construct_solution()
                solutions.append(solution)
                makespan = self.cloud_sim.calculate_makespan(solution)
                if makespan < best_makespan:
                    best_makespan = makespan
                    best_solution = solution

            self.update_pheromone(solutions)

        return best_solution

    def construct_solution(self):
        solution = []
        unassigned_tasks = list(range(self.cloud_sim.num_tasks))

        while unassigned_tasks:
            task = np.random.choice(unassigned_tasks)
            vm = self.select_vm(task)
            solution.append((task, vm))
            unassigned_tasks.remove(task)

        return solution

    def select_vm(self, task):
        probabilities = self.calculate_probabilities(task)
        return np.random.choice(range(self.cloud_sim.num_vms), p=probabilities)

    def calculate_probabilities(self, task):
        pheromone = self.pheromone[task]
        heuristic = 1 / (self.cloud_sim.execution_times[task] + 1e-10)
        probabilities = (pheromone ** self.alpha) * (heuristic ** self.beta)
        return probabilities / np.sum(probabilities)

    def update_pheromone(self, solutions):
        self.pheromone *= (1 - self.evaporation_rate)
        for solution in solutions:
            makespan = self.cloud_sim.calculate_makespan(solution)
            for task, vm in solution:
                self.pheromone[task, vm] += 1 / makespan