#--*-- coding: utf-8 --*--



def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x


def power(x, n=2):
    if n == 1:
        return x
    else:
        return x * power(x,n-1)


def power2(x,n):
    s = 1
    while n > 0:
        s *= x
        n -= 1
    return s

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    return sum


def person(name,age,**kw):
    print('name:',name,'age',age,'other',kw)


def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)

def findMinAndMax(*L):
    if L[0]>= L[1]:
        tmp=(L[0],L[1])
    else:
        tmp=(L[1],L[0])
    for i in L[2:]:
        if i > tmp[0]:
            tmp = (i,tmp[1])
        elif i < tmp[1]:
            tmp = (tmp[0],i)
        else:
            pass
    return tmp

def fib(n):
    i,a,b = 0,0,1
    while i < n:
        print(b)
        a,b = b,a+b
        i += 1
    else:
        return 'done'

def fib2(n):
    i,a,b = 0,0,1
    while i < n:
        yield(b)
        a,b = b,a+b
        i += 1
    else:
        return 'done'


def triangles(n):
    i=0
    L=[1]
    while i < n:
        if i == 0:
            i += 1
            yield(L)
        else:
            tmp=[1]
            tmp.extend([L[j] + L[j+1] for j in range(i) if j+1 < len(L)])
            tmp.append(1)
            L = tmp
            i += 1
            yield(L)
    else:
        return 'done'
