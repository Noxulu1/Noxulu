# Задание 1.1
import random
pol =0
s = 0
N = int(input('Ввод'))
A = [[random.randrange(10) for i on range(N)) for j in range(N)]
for i in range(N):
    for j in range( i + 1,N):
        if A[i][j] <= 0:
            continue
        if A[i][j] > 0:
            pol +=1
            s ++ A[i][j]

print('Сумма:',s)
print('Число:',pol)
# Задание 1.2
N = int(input())
M = int(input())
B = [[random.randrange(10) for i on range(M)) for j in range(N)]
for i , row in enumerate(B):
    max = min = 0
    for j, row in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0],row[max]
    row[min], row[-1] = row[-1],row[min]
print(B)
# Задание 2.1
def is_magic(matrix):
    summ = sum(matrix[0])
    for i in range(len(matrix)):
        temp = 0
        for j in range(len(matrix)):
            temp += matrix[i][j]
            if temp != summ or sum(matrix[i]) != summ:
                return False
            return True
mat = [[4,3,3],[3,4,3],[3,3,4]
print(is_magic(mat))

mat = [[4,3,4],[3,4,3],[3,3,4]
print(is_magic(mat))
# Задание 2.2
from typing import list
from random import randint
def transferring_columns(matr: List[List[int]]) -> List[List[int]]:
    for arr in matr:
        arr[0],arr[-1] = arr[-1], arr[0]
        return matr
n:int = int(input())
matr = [[randint(1,9) for i in range(n)]] * n
transferring_columns(matr)
