import numpy as np
def f(x):
    return x**2 + 5 * x + 6  
def f_prime(x):
    return 2 * x + 5
def line_search_method(x_start, direction, step_size, epsilon=1e-5, max_iterations=1000):
    x = x_start
    iteration = 0

    while iteration < max_iterations:
        gradient = f_prime(x)
        new_x = x + step_size * direction
        if np.abs(new_x - x) < epsilon or np.abs(gradient) < epsilon:
            break

        x = new_x
        iteration += 1

    return x, f(x)
x_start = 0
search_direction = -1
step = 0.1
optimal_solution, minimum_value = line_search_method(x_start, search_direction, step)

print("Optimal Solution (x):", optimal_solution)
print("Minimum Value of f(x):", minimum_value)
