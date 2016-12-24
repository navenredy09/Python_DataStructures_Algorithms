'''
Fibonacci Series:
f_1 = f_2 = 1
f_n = f_{n-1} + f_{n-2} for n > 2
'''

# A Direct implementation of this definition.
def fib(n):
  if n<=2:
    return 1
  else:
    return fib(n-1) + fib(n-2)

