# utils.py

import matplotlib.pyplot as plt
import numpy as np
import logging

def setup_logging():
    logging.basicConfig(filename='logs.txt', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def plot_results(aco_solution, abc_solution, cloud_sim):
    aco_loads = apply_solution(aco_solution, cloud_sim)
    abc_loads = apply_solution(abc_solution, cloud_sim)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

    x = np.arange(cloud_sim.num_vms)
    width = 0.35

    ax1.bar(x - width/2, aco_loads, width, label='ACO')
    ax1.bar(x + width/2, abc_loads, width, label='ABC')
    ax1.set_ylabel('Load')
    ax1.set_title('VM Loads Comparison')
    ax1.set_xticks(x)
    ax1.set_xticklabels([f'VM {i+1}' for i in range(cloud_sim.num_vms)])
    ax1.legend()

    aco_makespan = cloud_sim.calculate_makespan(aco_solution)
    abc_makespan = cloud_sim.calculate_makespan(abc_solution)
    
    ax2.bar(['ACO', 'ABC'], [aco_makespan, abc_makespan])
    ax2.set_ylabel('Makespan')
    ax2.set_title('Makespan Comparison')

    plt.tight_layout()
    plt.savefig('results_plot.png')
    plt.close()

    logging.info(f"Results plot saved as results_plot.png")

def apply_solution(solution, cloud_sim):
    vm_loads = [0] * cloud_sim.num_vms
    for task, vm in solution:
        vm_loads[vm] += cloud_sim.get_task_execution_time(task, vm)
    return vm_loads

def calculate_load_imbalance(solution, cloud_sim):
    vm_loads = apply_solution(solution, cloud_sim)
    avg_load = sum(vm_loads) / len(vm_loads)
    max_load = max(vm_loads)
    return (max_load - avg_load) / avg_load

def log_solution_stats(solution, cloud_sim, algorithm_name):
    makespan = cloud_sim.calculate_makespan(solution)
    imbalance = calculate_load_imbalance(solution, cloud_sim)
    logging.info(f"{algorithm_name} Results:")
    logging.info(f"  Makespan: {makespan}")
    logging.info(f"  Load Imbalance: {imbalance:.2f}")