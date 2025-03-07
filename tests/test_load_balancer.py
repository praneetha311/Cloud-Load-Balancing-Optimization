import unittest
from src.load_balancer import LoadBalancer
from src.cloudsim import CloudSimulator

class TestLoadBalancer(unittest.TestCase):
    def setUp(self):
        self.cloud_sim = CloudSimulator(num_vms=5, num_tasks=10, seed=42)
        self.load_balancer = LoadBalancer(self.cloud_sim)

    def test_calculate_makespan(self):
        solution = [(i, i % 5) for i in range(10)]  # Distribute tasks evenly
        makespan = self.load_balancer.calculate_makespan(solution)
        self.assertGreater(makespan, 0)

    def test_apply_solution(self):
        solution = [(i, i % 5) for i in range(10)]
        vm_loads = self.load_balancer.apply_solution(solution)
        self.assertEqual(len(vm_loads), 5)
        self.assertTrue(all(load > 0 for load in vm_loads))

    def test_get_vm_utilization(self):
        solution = [(i, i % 5) for i in range(10)]
        utilization = self.load_balancer.get_vm_utilization(solution)
        self.assertEqual(len(utilization), 5)
        self.assertAlmostEqual(sum(utilization), 1.0, places=5)

if __name__ == '__main__':
    unittest.main()