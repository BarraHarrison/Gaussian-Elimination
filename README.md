# **Gaussian Elimination 🚀**  

## **Introduction 🎯**  
This project is a hands-on exploration of **Gaussian Elimination**, a fundamental method used in linear algebra to solve systems of equations. The goal of this project is to break down the process step by step and compare it with NumPy’s built-in **Linear Algebra (`linalg`) library**.  

---

## **What is Gaussian Elimination? 🤔**  
Gaussian Elimination is a method used to solve **systems of linear equations**. It transforms a system of equations into a simpler form, making it easier to find the values of unknown variables. The process involves:  

1. **Converting the system into an upper triangular matrix** – This means making the numbers below the main diagonal **zero** by performing row operations.  
2. **Back-substitution** – Once the matrix is in the right form, work your way **backward** to find the solution.  

Think of it like solving a puzzle: Break the problem into smaller, simpler steps until the answer becomes obvious!  

---

## **NumPy Linear Algebra Library 🏗️**  
Python’s **NumPy** library provides a powerful built-in function to solve systems of equations:  

```python
solution = np.linalg.solve(A, B)
```
This function automatically applies **Gaussian Elimination** behind the scenes, making it extremely efficient and reliable. It also handles special cases where a system has **no solution** or **infinite solutions**, raising an error if needed.  

While NumPy is great for quick calculations, understanding what’s happening under the hood is essential.

---

## **Creating the `gaussian_elimination` Function 📌**  
In this project, I implemented **Gaussian Elimination from scratch** without relying on NumPy’s built-in solver. Here’s how the function solves the problem:  

### **Step 1: Create an Augmented Matrix**  
Combine the coefficient matrix `A` and the solution vector `B` into a single **augmented matrix**, making it easier to apply row operations.  

### **Step 2: Forward Elimination (Making a Triangular Matrix) 🔺**  
- Go row by row and eliminate values below the **main diagonal** to create an **upper triangular matrix**.  
- This is done by selecting a **pivot element** (the leading nonzero number in each row) and using it to eliminate the numbers below it.  

### **Step 3: Partial Pivoting (Avoiding Errors) 🔄**  
- If the pivot is too close to zero, then **swap rows** to ensure numerical stability and avoid division errors.  

### **Step 4: Back-Substitution (Finding the Answers) ✅**  
- Once there is upper triangular matrix, solve for the unknown variables **starting from the last row** and working upwards.  

By following these steps, the function successfully finds the solution, just like NumPy’s `linalg.solve()`, but now I understand **how** it works under the hood!  

---

## **Conclusion 🎓**  
Gaussian Elimination is a powerful tool in linear algebra, but it can seem complicated at first. By coding it from scratch, break down each step, making it easier to understand.  

While **NumPy’s built-in functions** handle these calculations efficiently, knowing the fundamentals helps in debugging, optimization, and deeper learning in mathematics and data science. 