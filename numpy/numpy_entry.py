import numpy as np

array1 = np.arange(6)
print(array1)
np.save("array1",array1)

np.load("array1.npy")
array2 = np.arange(8)

np.savez("arrays",x=array1,y=array2)
array_recuperado = np.load("arrays.npz")
print(array_recuperado['y'])

np.savetxt('mificheroarray.txt',array2,delimiter=',')

np.loadtxt('mificheroarray.txt',delimiter=',')