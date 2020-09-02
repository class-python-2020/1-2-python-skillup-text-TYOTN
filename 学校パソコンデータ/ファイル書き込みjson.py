import json

data={"no":313,"code":("秋山",9,181,9,66.3,335),"scr":"「諦めない」って口で言うほど簡単なことじゃねぇよ"
}

filename = "test.json"
with open(filename,"w",encoding="utf-8")as fp:
    json.dump(data,fp)