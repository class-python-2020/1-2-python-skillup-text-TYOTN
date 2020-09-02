file = open("sample.txt",encoding="utf-8")
lines = file.readlines()

file.close()

print(lines)