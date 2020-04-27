'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.

Example

Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''

row = int(input("Enter rows: "))
column = int(input("Enter columns: "))

row_lst = []
column_lst = []

for i in range(0,row):
    row_lst.append(i)

for j in range(0,column):
    column_lst.append(j)

new_lst = []
final_lst = []
for k in row_lst:
# 0,1,2    
    for l in column_lst:
# 0,1,2,3,4
        new_lst.append(k*l)
        final_lst.append(new_lst)
print(final_lst)


