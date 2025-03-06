# Coding out Gaussian-Elimination to understand it better
import numpy as np 

def solve_system_of_equations(A, B):
    try:
        solution = np.linalg.solve(A, B)
        return solution
    except np.linalg.LinAlgError:
        return "System does not have a solution"