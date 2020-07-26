# Uses python3
def naive_fib(n):
    """slow execution due to multiple recursive calls"""
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)
def calc_fib(n):
    """fast and better algo for fibonacci series"""
    if n<=1:
        return n
    fib = [0]*n
    fib[0],fib[1] = 1,1
    for i in range(2,n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n-1]

n = int(input())
print(calc_fib(n))
