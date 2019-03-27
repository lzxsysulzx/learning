import numpy as np
a=np.array([1,2,3,4])
print("a =",a)
b=np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print("b =\n", b)
print("dtype of b =", b.dtype)
print("shape of a =", a.shape)
print("shape of b =", b.shape)
c=b.reshape((4,3))
print("c =\n",c)
b[0][2]=100
print("b =\n", b)
print("c =\n", c)
