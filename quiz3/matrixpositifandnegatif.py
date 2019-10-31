import numpy as np
m = int(input("Masukkan m: "))
n = int(input("Masukkan n: "))
random_matrix_array = np.random.randint(m*n,size=(m,n))
if list(random_matrix_array >=0 ):
    print("bilangan positif")
else:
    print("bilangan negatif")
print(random_matrix_array)


