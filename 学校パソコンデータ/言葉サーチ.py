import re 

s= "1 taro , 2 jiro # 3 hana"

match_list = re.findall(r"\d+\s+\w+",s)
print(match_list)