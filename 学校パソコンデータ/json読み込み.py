import json
filename = "test.json"
with open(filename,"r",encoding="utf-8") as fp:
    r =json.load(fp)
    print("no=",r["no"])
    print("code=",r["code"])
    print("scr=",r["scr"])