import sys
rc_limit= sys.getrecursionlimit()
print(rc_limit)

def fact (n):
    if n ==1 :
        return 1
    else:
        return (n * fact(n-1))
a = rc_limit
print(f'{a}の階乗は{fact(a):4}')