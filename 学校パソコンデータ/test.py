import re

s= "電話番号 019-622-1500 郵便番号 ０２０ー００２１です"

a_list = re.findall(r"\d+",s)
print(a_list)