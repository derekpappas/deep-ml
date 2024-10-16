import math

from src.svd import result


def sigmoid(z: float) -> float:
  sigma_x = math.exp(-z)
  sigmoid_x = 1 / (1 + sigma_x)
  result = round(sigmoid_x, 3)
  return result

z = 0

print(f"sigmoid({z}) = {sigmoid(z)}")

z = 1

print(f"sigmoid({z}) = {sigmoid(z)}")

z = -1

print(f"sigmoid({z}) = {sigmoid(z)}")

z = 10

print(f"sigmoid({z}) = {sigmoid(z)}")

z = -10

print(f"sigmoid({z}) = {sigmoid(z)}")

z = 2.718281828459045

print(f"sigmoid({z}) = {sigmoid(z)}")



