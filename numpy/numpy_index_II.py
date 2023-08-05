import numpy as np

array1 = np.arange(0,11)
print(array1)

print(array1[0:3])
print(array1[:])
array_copia = array1.copy()
print("==============")
array_copia[0:3] = 20
print(array_copia)
print(array1)



array2 = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(array2)
print(array2[2][:])
print(array2[2])