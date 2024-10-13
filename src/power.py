import torch

x = [4,5,6]
print('x = ' + str(x))

x_ten = torch.tensor(x)
print('torch.tensor(x) = ' + str(x_ten))

# The power function torch.pow also accepts tensors as the exponent argument. Start by expanding your input tensor x, column-wise:

# tensor([[4, 4, 4],
#         [5, 5, 5],
#         [6, 6, 6]])
# Then define your exponents as a range tensor:

xr = x_ten[:,None]
print('xr = ' + str(xr) + '\n')

xre = xr.expand(-1,3)
print('xr.expand(-1,3) = ' + str(xre) + '\n')

# tensor([1, 2, 3])
# And compute your power tensor:

a = torch.arange(1,4)
print('torch.arange(1,4) = ' + str(a) + '\n')

# tensor([[  4,   5,   6],
#         [ 16,  25,  36],
#         [ 64, 125, 216]])

xre_pow = xre.pow(a)
print('xre.pow(a) = ' + str(xre_pow) + '\n')

xre_pow_T = xre_pow.T
print('xre_pow_T = ' + str(xre_pow_T) + '\n')