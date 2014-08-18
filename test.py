# def funcD(a, b,*f, **c):
#     print a
#     print b
#     print f
#     for x in c:
#         print x + ':' + str(c[x])
# funcD(1,2,3,c=2,e=1,x=4)

# #f(n) = 1,2,3,5,8,13,...,n
# def fib(n):
#     a,b=0,1
#     while a<n:
#         print a,
#         a,b=b,a+b
# fib(100)

# #n!
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# x = int(raw_input("Calculator n! \nplease input a num:"))
# print x,'! = ',fact(x)