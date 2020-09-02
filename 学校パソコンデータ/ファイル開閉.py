search_key="オブジェクト"
with open("sample.txt",encoding = "utf-8")as file:
    for i,line in enumerate(file):
        if line.find(search_key)>=0:
            print(f'{i+1}行目{line.find(search_key)}文字目にありました！')
            print(f'{line}')