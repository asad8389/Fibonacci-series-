# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    """slow naive approch"""
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fib_pis(from_,to):
    """its a bit longer in terms of lines
    but much faster than the previous one"""
    from_%=60
    to%=60

    sum = 0

    current = 0
    next  = 1
    if from_<=to:
        for i in range(to + 1):
            if i >= from_:
                sum += current

            current, next = next, current + next
    else:
        for i in range(61):
            if i >= from_:
                sum += current

            current, next = next, current + next
        current, next= 0,1
        for i in range(to+1):
            sum += current

            current, next = next, current + next
    
    return sum%10

    
if __name__ == '__main__':
    #input = sys.stdin.read();
    from_, to = map(int, input().split())
    print(fib_pis(from_, to))
