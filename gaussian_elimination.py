# Coding out Gaussian-Elimination to understand it better
import numpy as np 

def solve_system_of_equations(A, B):
    try:
        solution = np.linalg.solve(A, B)
        return solution
    except np.linalg.LinAlgError:
        return "System does not have a solution"
    
A = np.array([
    [3, -1, -1],
    [1, 1, 0],
    [2, 0, -3]
])

B = np.array([5, 0, 2])

print(solve_system_of_equations(A, B))
# Result: [ 1.3 -1.3  0.2]