def word_quiz(word): #ジェネレータの定義
    hint = ""
    for letter in word:#引数で置け取った文字列から１文字ずつ取り出す
            hint += letter  #先に取り出した文字に連結していく
            yield hint #ヒントを返す　
            #これまで取り出した分の文字列を次の値として返す

ans = "Python" #出題する
quiz = word_quiz(ans)  #ジェネレータを作る

while True:
    try:#try とexceptを利用することで、最後に終了ですに飛べる。
        hint = next(quiz)
        print(hint)
        
        word = input(f"この単語は（{len(ans)}文字）？:")
        if ans.lower() == word.lower():
            print("正解です。おめでとう")
            break
        else:
            print("違います")
    except :#try　でエラーを発生させたときこっちに飛ぶ。
        print("終了です。")
        break