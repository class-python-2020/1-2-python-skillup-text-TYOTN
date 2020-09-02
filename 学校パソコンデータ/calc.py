def calc(func , arg=1):
    price = func(arg)  #引数で受け取った関数funcとargを実行する
    return price
     
def child(arg): #calcに渡して実行する関数
    return 400 * arg

def adult(arg): #calcに渡して実行する関数
    return 800 * arg

age = int(input("何歳ですか?>"))
num = int(input("何人ですか?>"))
if age < 16 : 
    price = calc (child, num) #child()関数を渡して計算する
else :
    price = calc (adult, num) #adult()関数を渡して計算する  
print(f"{age}歳、{num}人は{price}円です")