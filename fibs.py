def fib1(n):
    result=[0,1]
    for i in range(n-2):
        result.append(result[-2]+result[-1])
    return result

def fib2(n):
    a, b = 0, 1
    result=[]
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

a1 = fib1(10)
a2 = fib2(100)
print(a1,a2)