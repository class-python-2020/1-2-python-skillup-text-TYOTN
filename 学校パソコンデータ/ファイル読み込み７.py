def show_wordlist(file):
    word_list=[]
    file_data = open(file)
    for line in file_data:
        tmp_list = line.split()

    for word in tmp_list:
        word = word.rstrip('.,:!?"')
        word = word.lstrip('("')
        if not word in word_list:
            word_list.append(word)
    return word_list

if __name__ == '__main__':
    file_name = input('ファイル名を入力してください＞＞＞')
    lst = show_wordlist(file_name)
    for word in lst:
        print(word)