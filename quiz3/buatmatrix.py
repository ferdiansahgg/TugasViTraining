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

while(num < len(mat)): 
    # checking condition 
    if mat[num] >= 0: 
        pos_count += 1
    else: 
        neg_count += 1
    # increment num  
    num += 1
print("Positive numbers in the list: ", pos_count) 
print("Negative numbers in the list: ", neg_count) 





# mat.sort()
# pos_count = len(list(filter(lambda x: (x >= 0), mat)))
# print("Positive numbers : ", pos_count)
# mat.sort()
# neg_count = len(list(filter(lambda x: (x < 0), mat)))
# print("Negative numbers : ", neg_count)

# for i in mat:
#     if (i > 0):
#         Positive_count +=1
#     elif (i < 0):
#         Negative_count +=1  
# print("Bilangan positif ada :",Positive_count)
# print("Bilangan Negative ada :",Negative_count)



