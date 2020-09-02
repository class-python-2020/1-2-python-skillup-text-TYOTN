def add(a:int,b:int)->int:
    result = 0
    try:
        result = a+b
    except TypeError as e:
        print(f'計算できませんでした{e}')
    return result

if __name__=='__mian__':
    result = add(100,200)
    print(result)