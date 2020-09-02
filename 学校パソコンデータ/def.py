import sys
#do()に渡して実行する関数
def English():    print("サンキュー")
def France():    print("メルスィーボクー")
def Germany():    print("ダンケ　シェーン")
def Japan():    print("ありがとう")
#引数で受け取った関数を実行する
def do(func):
    func()
#コマンドラインから文字列を受け取る
args = sys.argv[1:]
#文字列を受け取っていたら…
if len(args) != 0: 
    print(args)
    if args[0] == 'E' :do(English)
    elif args[0] == 'F' :do(France)
    elif args[0] == 'G' :do(Germany)
    else :do(Japan)