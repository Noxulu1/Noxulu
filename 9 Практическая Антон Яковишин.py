# 9 Практика БЛОК A.1 задание
def calc_expression(x,n):
    if n == 0:
        return 1
    return ( x ** n)/ factorial(n) + calc_expression(x,n - 1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n -1 )

x = int(input('ВВедите значение x: '))
n = int(input('ВВедите значение n: '))
# 9 Практика БЛОК B.3 задание
def f():
    s = [int(i) for i in input('Введите данные:').split() if int(i)]
    print(*s[::2])

