from scipy.optimize import fsolve
import numpy as np
def derivative(x):
    return 10 * np.pi * np.sin(np.pi * x - 2.2) + 2 * x + 1.5
critical_points = fsolve(derivative, [-2, 2])  
values_at_critical_points = -10 * np.cos(np.pi * critical_points - 2.2) + (critical_points + 1.5) * critical_points
global_min_index = np.argmin(values_at_critical_points)
global_optimal_solution = critical_points[global_min_index]
min_function_value = values_at_critical_points[global_min_index]
print("Critical Points:", critical_points)
print("Function Values at Critical Points:", values_at_critical_points)
print("Global Optimal Solution (Minimum):", global_optimal_solution)
print("Minimum Function Value:", min_function_value)
