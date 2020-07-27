# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    """ this is the basic solution that
    is not very efficient for big values of n"""
    fib = [0 for i in range(n)]
    fib[0],fib[1] = 1,1
    for i in range(2,n):
        fib[i] = (fib[i-1] + fib[i-2])%10
    return fib[n-1]

def get_fibonacci_last_digit_fast(n):
    """ pianso period is a number at which
    last digit of fibonacci series starts repeating"""
    
    pisano_period = 60
    n = n%pisano_period

    if n==0:
        return 0
    
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current%10

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_fast(n))
