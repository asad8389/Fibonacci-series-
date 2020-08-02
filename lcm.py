# Uses python3
import sys

def lcm_algo(a, b):

    global lcm
    if gcd(a,b)==1:
        return lcm*a*b
    else:
        x = gcd(a,b)
        lcm*=x
        return lcm_algo(a//x,b//x)
        
def gcd(a,b):
    if b==0:
        return a

    if b>a:
        a,b=b,a
    x = a%b

    return gcd(b,x)


    
if __name__ == '__main__':
    #input = sys.stdin.read()
    a, b = map(int, input().split())
    lcm=1
    print(lcm_algo(a, b))

