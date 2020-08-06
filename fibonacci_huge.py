# Uses python3
import sys

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    ps_prd = pisano(m)
    n = n%ps_prd
    if n<=1:
        return n
    for _ in range(n-1):
        previous, current = current, previous + current

    return current % m
def pisano(m):
    p, c =0,1
    for i in range(m*m):
        p , c = c, (p+c)%m

        if p==0 and c==1:
            return i+1
if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge(n, m))
