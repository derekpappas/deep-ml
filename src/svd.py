import numpy as np

# https://stackoverflow.com/questions/75873083/pytorch-generate-polynomials-of-a-vector

A = np.array([[-10, 8],
              [10, -1]])

print('A = ' + str(A))

AT = A.T

print('AT = ' + str(AT))

AAT = np.dot(A, AT)

AAT = np.dot(A, AT)
print('AAT = ' + str(AAT))

a = AAT[0][0]
b = AAT[0][1]
c = AAT[1][0]
d = AAT[1][1]

print('a = ' + str(a))
print('b = ' + str(b))
print('c = ' + str(c))
print('d = ' + str(d))

ad = a * d
bc = b * c
ad_bc = ad - bc

print('ad = ' + str(ad))
print('bc = ' + str(bc))
print('ad_bc = ' + str(ad_bc))

ad = a + d

z = [ad_bc, ad, 1]

print('z = ' + str(z))

# Create a polynomial object
p = np.poly1d(z)

# Print the polynomial
print("Polynomial:")
print(p)

print('np.poly1d = ' + str(np.poly1d(p)))

# Find the roots of the polynomial
roots = np.roots(z)

# Print the roots
print("\nRoots:")
print(roots)

# Verify the roots
print("\nVerifying roots:")
for root in roots:
    result = p(root)
    print(f"p({root}) = {result}")
# abs() is used to handle floating point errors
roots = np.abs(roots)

# Find the common square root of the roots
common_roots = np.sqrt(roots)
print("\nCommon square root of the roots:")
print(common_roots)

evalues, evectors = np.linalg.eig(AAT)
print('evalues = ' + str(evalues))
print('\nevectors = ' + str(evectors))

# # Calculate 1/roots to get the original roots
# print("\nOriginal roots (1/calculated roots):")
# original_roots = 1 / roots
# print(original_roots)
#
# # abs() is used to handle floating point errors
# original_roots = np.abs(original_roots)
#
# S = []
# for root in original_roots:
#   print(f"root = {root}")
#   result = np.sqrt(root)
#   print(f"np.sqrt({root}) = {result}")
#   S.append(result)
#
# print('S = ' + str(S))
#
