import unittest
from src.aco import AntColonyOptimization
from src.cloudsim import CloudSimulator

class TestAntColonyOptimization(unittest.TestCase):
    def setUp(self):
        self.cloud_sim = CloudSimulator(num_vms=5, num_tasks=10, seed=42)
        self.aco = AntColonyOptimization(self.cloud_sim, num_ants=10, num_iterations=20)

    def test_optimize(self):
        solution = self.aco.optimize()
        self.assertEqual(len(solution), 10)
        self.assertTrue(all(0 <= vm < 5 for _, vm in solution))

    def test_construct_solution(self):
        solution = self.aco.construct_solution()
        self.assertEqual(len(solution), 10)
        self.assertTrue(all(0 <= vm < 5 for _, vm in solution))

    def test_update_pheromone(self):
        initial_pheromone = self.aco.pheromone.copy()
        solutions = [self.aco.construct_solution() for _ in range(5)]
        self.aco.update_pheromone(solutions)
        self.assertFalse(np.array_equal(initial_pheromone, self.aco.pheromone))

if __name__ == '__main__':
    unittest.main()