# https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if (x1>x2 and v1>v2) or (x2>x1 and v2>v1):
        return "NO"
    d1=x1
    d2=x2
    for i in range(10001):
        d1=d1+v1
        d2=d2+v2
        if d1==d2:
            return "YES"
    return "NO"