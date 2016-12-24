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
  
# Using DP
def fib_dp(n):
    fib_values = [0,1]
    for i in range(2,n+1):
        fib_values.append(fib_values[i-1] + fib_values[i-2])
    return fib_values[n]

if __name__ == "__main__":
  fib(100)        #this algorithm seems to never terminate!
  fib_dp(100)     #It's a magic 354224848179261915075
  

