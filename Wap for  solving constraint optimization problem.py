from scipy.optimize import minimize
def objective_function(variables):
    x, y = variables
    return x**2 + y**2
def inequality_constraints(variables):
    x, y = variables
    return [
        1 - 2*x - y, 
        2 - x - 3*y 
initial_guess = [0.5, 0.5] 
bounds = [(0, None), (0, None)] 
constraints = {'type': 'ineq', 'fun': inequality_constraints}
result = minimize(objective_function, initial_guess, bounds=bounds, constraints=constraints)
print("Optimal Solution (x, y):", result.x)
print("Minimum Value of f(x, y):", result.fun)
