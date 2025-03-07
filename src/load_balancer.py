# load_balancer.py

class LoadBalancer:
    def __init__(self, cloud_sim):
        self.cloud_sim = cloud_sim

    def calculate_makespan(self, solution):
        return self.cloud_sim.calculate_makespan(solution)

    def apply_solution(self, solution):
        vm_loads = [0] * self.cloud_sim.num_vms
        for task, vm in solution:
            vm_loads[vm] += self.cloud_sim.execution_times[task]
        return vm_loads

    def get_vm_utilization(self, solution):
        vm_loads = self.apply_solution(solution)
        total_load = sum(vm_loads)
        return [load / total_load for load in vm_loads]