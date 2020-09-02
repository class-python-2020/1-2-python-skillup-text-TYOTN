file =open ("turezure.txt",encoding= "sjis")

s= file.read()#ファイルの読み書きをする　read()かwrite()

file.close()#ファイルを閉じる

print(s)
