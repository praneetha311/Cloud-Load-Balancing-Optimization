# main.py

from aco import AntColonyOptimization
from artificial_bee_colony import ArtificialBeeColony
from load_balancer import LoadBalancer
from cloudsim import CloudSimulator
from utils import plot_results, log_solution_stats, setup_logging

def main():
    # Setup logging
    setup_logging()

    # Initialize the cloud simulator
    cloud_sim = CloudSimulator(num_vms=10, num_tasks=100)

    # Initialize load balancer
    load_balancer = LoadBalancer(cloud_sim)

    # Run ACO optimization
    aco = AntColonyOptimization(cloud_sim, num_ants=20, num_iterations=50)
    aco_solution = aco.optimize()
    log_solution_stats(aco_solution, cloud_sim, "ACO")

    # Run ABC optimization
    abc = ArtificialBeeColony(cloud_sim, num_bees=20, num_iterations=50)
    abc_solution = abc.optimize()
    log_solution_stats(abc_solution, cloud_sim, "ABC")

    # Plot and save results
    plot_results(aco_solution, abc_solution, cloud_sim)

if __name__ == "__main__":
    main()