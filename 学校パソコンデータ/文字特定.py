import re 
line = "そういやパイソンはどうなった？"

m = re.search("いや",line)
print(m.group())
#いや
print(m.span())
print(m)