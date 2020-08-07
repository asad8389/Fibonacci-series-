# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    """slow naive approch"""
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10
def fib(n):
    """fast and better in this we've multiplied the fn with fn-1"""
    n = n%60
    p,c = 0,1
    for i in range(n):
        p, c = c, c+p
    return (c*p)%10






    
if __name__ == '__main__':
    n = int(input())
    print(fib(n))
