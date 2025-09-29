import numpy as np

# Создание матриц
A = np.array([[3, 2, 4],
              [1, 7, 2]])

B = np.array([[3, 4],
              [2, 3],
              [8, 5]])

# Умножение матриц
result = np.dot(A, B)
# Или используя оператор @ (Python 3.5+)
# result = A @ B

print("Матрица A:")
print(A)
print("\nМатрица B:")
print(B)
print("\nРезультат умножения A × B:")
print(result)
