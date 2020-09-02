def simFib(n):
    if(n<=2):
        return 1
    else:
        return simFib(n-2) + simFib(n-1)
for i in range(1,10):
    print(f"{simFib(i)}",end="")