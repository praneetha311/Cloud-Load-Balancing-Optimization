# cloudsim.py

import numpy as np

class CloudSimulator:
    def __init__(self, num_vms, num_tasks, seed=42):
        self.num_vms = num_vms
        self.num_tasks = num_tasks
        np.random.seed(seed)
        
        # Generate random execution times for tasks on VMs
        self.execution_times = np.random.randint(1, 100, size=(num_tasks, num_vms))

    def calculate_makespan(self, solution):
        vm_loads = [0] * self.num_vms
        for task, vm in solution:
            vm_loads[vm] += self.execution_times[task, vm]
        return max(vm_loads)

    def get_task_execution_time(self, task, vm):
        return self.execution_times[task, vm]

    def get_total_execution_time(self):
        return np.sum(self.execution_times)