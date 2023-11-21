#Вариант 14.1
def deli(n): 
    l, m = 0, int(n**0.5) 
    for i in range(1, m + 1): 
	if n % i == 0: l += 2 
    if m * m == n: l -= 1 
    return l 
while True: 
    M, N = map(int, input('M N: ').split()) 
    maxi, num = 0, [] 
    for i in range(M, N + 1): 
	d = deli(i) 
	if d > maxi: maxi = d; num = [i] 
	elif d == maxi: num.append(i) 
    print('Количество делителей:', d) 
    print(*num)
#Вариант 14.2
def min_dist(x,y,z):
    def dist(a,b):
        return (a[0]-b[0])**2+(a[1]-b[1])**+2(a[2]-b[2])**2
    n=len(x)
    dmin=dist((x[0],y[0],z[0]),(x[1],y[1],z[1]))
    for i in range(n):
        for j in range(i+1,n+1):
            d=dist((x[i],y[i],z[i]),(x[j],y[j],z[j]))
            id d<dmin:
                dmin=d
                imin=i
                jmin=j
    return (imin,jmin,dmin**0.5)
    
#3.1
def hypotenuse(a,b):
    return sqrt(a**2 + b**2)

if hypotenuse(5,10) > hypotenuse(10,15):
    print('Первая гипотенуза больше')
else:
    print('Первая гипотенуза меньше')
#3.2
s = ['t','z','b','u','a']

s.sort()
print(s)
