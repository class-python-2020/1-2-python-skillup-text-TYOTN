import re

line = "ねえ、今日はごはん何かな"

m = re.search(r'ごはん|今日|はぶ',line)

print(m.group())
