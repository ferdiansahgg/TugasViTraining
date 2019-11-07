m = int(input("Enter number of row : "))
n = int(input("Enter number of column : "))
mat= []
num = 0
pos_count = 0
neg_count = 0
# Positive_count = 0
# Negative_count = 0
for i in range (0,m):
    mat.append([])
for i in range (0,m):
    for j in range(0,n):
        mat[i].append(j)
        mat[i] [j]=0
for i in range (0,m):
    for j in range (0,n):
        print ('Entry in row: ', i+1, 'column: ', j+1)
        mat[i][j]= int(input()) 

print(mat)

for i in range(0, len(mat)):
    print(mat[i], "|...|", mat[i])
print()






