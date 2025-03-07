import unittest
from src.artificial_bee_colony import ArtificialBeeColony
from src.cloudsim import CloudSimulator

class TestArtificialBeeColony(unittest.TestCase):
    def setUp(self):
        self.cloud_sim = CloudSimulator(num_vms=5, num_tasks=10, seed=42)
        self.abc = ArtificialBeeColony(self.cloud_sim, num_bees=10, num_iterations=20)

    def test_optimize(self):
        solution = self.abc.optimize()
        self.assertEqual(len(solution), 10)
        self.assertTrue(all(0 <= vm < 5 for _, vm in solution))

    def test_generate_random_solution(self):
        solution = self.abc.generate_random_solution()
        self.assertEqual(len(solution), 10)
        self.assertTrue(all(0 <= vm < 5 for _, vm in solution))

    def test_calculate_fitness(self):
        solution = self.abc.generate_random_solution()
        fitness = self.abc.calculate_fitness(solution)
        self.assertGreater(fitness, 0)
        self.assertLess(fitness, 1)

if __name__ == '__main__':
    unittest.main()