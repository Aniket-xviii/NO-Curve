import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x
x_values = np.linspace(-5, 5, 1000)
y_values = f(x_values)
optimal_x = x_values[np.argmin(y_values)]
optimal_y = np.min(y_values)
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=r'$f(x)=-10\cos(\pi x - 2.2)+(x+1.5)x$')
plt.scatter(optimal_x, optimal_y, color='red', label='Global Optimal Solution')
plt.title('Graph of f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
print("Global Optimal Solution (x):", optimal_x)
print("Minimum Value of f(x):", optimal_y)
