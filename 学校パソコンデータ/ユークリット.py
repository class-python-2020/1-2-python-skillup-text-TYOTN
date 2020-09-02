def gcd(a,b):
    if (b==0):
        return a
    else:
        return (gcd(b,a%b))

print(gcd(72,32))
print(gcd(456,276))
print(gcd(753892,491))