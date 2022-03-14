# Write a python program to print a 3x3 formatted matrix as shown below, using lists and nested loops.
# Make note of 2d array, loop/iteration and zero based counting.
# matrix = [ [1,2,3],[4,5,6],[7,8,9] ] #write a function to output the formatted matrix :
# 1 2 3
# 4 5 6
# 7 8 9

matrix = [ [1,2,3],[4,5,6],[7,8,9] ]

# print each sublist in new row
# for row in matrix:
#   print (row, sep=',')
# a = matrix[0
# print(a)

a = matrix[0][0], matrix[0][1], matrix[0][2]
b = matrix[1][0], matrix[1][1], matrix[1][2]
c = matrix[2][0], matrix[2][1], matrix[2][2]
print(*a, sep=" ")
print(*b, sep=" ")
print(*c, sep=" ")

for i in matrix:
  print(str(i).replace('[', '').replace('[', '').replace(']', ''))
