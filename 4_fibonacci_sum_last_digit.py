# Uses python3
import sys

def fibonacci_sum_naive(n):
    """ this is a naive solution, it takes alot of time in execution"""
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fib_sum_fast(n):
    """"this is a faster algo which uses pisano number"""
    p, c= 0, 1
    pis = 60        #pisano no for 10

    n = n%pis
    s=1
    if n==0:
        return 0
    for _ in range(n-1):
        p, c = c, p + c
        s += c
    return s%10


if __name__ == '__main__':
    n = int(input())
    print(fib_sum_fast(n))
