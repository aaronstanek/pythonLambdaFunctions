fibonacci = (lambda a,b : lambda x : a(b,x))(lambda b,x : -1 if type(x) != int else -1 if x < 0 else x if x < 2 else b(b,x,1,1,2), lambda b,x,p,q,h : p + q if h == x else b(b,x,q,p+q,h+1))
# fibonacci(n) returns the nth fibonacci number
# time : O(n)

factorial = (lambda a,b : lambda x : a(b,x))(lambda b,x : -1 if type(x) != int else -1 if x < 0 else b(b,x), lambda b,x : 1 if x == 0 else x*b(b,x-1))
# factorial(n) returns n!
# time : O(n)

ackermann = (lambda a,b : lambda m,n : a(b,m,n))(lambda b,m,n : -1 if type(m) != int or type(n) != int else -1 if m < 0 or n < 0 else b(b,m,n), lambda b,m,n : n + 1 if m == 0 else b(b,m-1,1) if n == 0 else b(b,m-1,b(b,m,n-1)))
# ackermann(m,n) returns the ackermann function evalutated at m,n
# you may need to use sys.setrecursionlimit to increase Python's recurison limit
# time : O(it will terminate eventually)

golden_ratio_num = (lambda a,b : lambda n : a(b,n))(lambda b,n : -1 if type(n) != int else -1 if n < 0 else b(b,n), lambda b,n : 1 if n == 0 else 1/b(b,n-1)+1)
# golden_ratio_num(n) returns an approximation of the golden ratio
# larger n produces better approximation
# time : O(n)

e_num = (lambda a,b : lambda n : a(b,n))(lambda b,n : -1 if type(n) != int else -1 if n < 0 else n if n < 2 else 2+b(b,n-2,2,3), lambda b,n,d,f : 0 if n == 0 else 1/d + b(b,n-1,d*f,f+1))
# e_num(n) returns an approximation of e
# larger n produces better approximation
# time : O(n)

pi_num = (lambda a,b : lambda n : a(b,n))(lambda b,n : -1 if type(n) != int else -1 if n < 0 else 3 + 1/b(b,n,3), lambda b,n,v : 6 if n == 0 else 6 + (v**2) / b(b,n-1,v+2))
# pi_num(n) returns an approximation of pi
# larger n produces better approximation
# time : O(n)
