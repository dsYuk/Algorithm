import torch
import numpy as np

data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(data)

np_array = np.array(data)
x_np = torch.from_numpy(np_array)

x_ones = torch.ones_like(x_data)
print(f"Ones Tensor: \n {x_ones}\n")

x_rand = torch.rand_like(x_data, dtype = torch.float)
print(f"Random Tensor: \n {x_rand}\n")

shape = (2, 3, )
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)
print(f"Random Tensor: \n {zeros_tensor} \n")

tensor = torch.rand(3, 4)
print(f"shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stores on: {tensor.device}")

if torch.cuda.is_available():
    tensor = tensor.to("cuda")

tensor = torch.ones(4, 4)
print(f"First row: {tensor[0]}")
print(f"first column: {tensor[:, 0]}")
print(f"Last columns: {tensor[..., -1]}")
tensor[:, 1] = 0
print(tensor)

t1 = torch.cat([tensor, tensor, tensor], dim = 1)  # tensor를 행으로 연결
print(t1)

t2 = torch.stack([tensor, tensor, tensor], dim = 0)  # tensor를 열로 연결
print(t2)

y1 = tensor @ tensor.T      # tensor.T = 역행렬
y2 = tensor.matmul(tensor.T)        # 행렬 곱 y1, y2, y3 모두 같음
y3 = torch.rand_like(y1)
torch.matmul(tensor, tensor.T, out = y3)

z1 = tensor * tensor        # 요소별 곱
z2 = tensor.mul(tensor)
z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out = z3)

agg = tensor.sum()
agg_item = agg.item()
print(agg_item, type(agg_item))

print(tensor)
tensor.add_(5)  # inplace 연산 -  자료에 직접적으로 영향을 주므로 잘 사용하지 않음

## numpy 변환
# tensor -> numpy
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

t.add_(1)
print(n)

# numpy -> tensor
n = np.ones(5)
t = torch.from_numpy(n)
np.add(n, 1, out = n)