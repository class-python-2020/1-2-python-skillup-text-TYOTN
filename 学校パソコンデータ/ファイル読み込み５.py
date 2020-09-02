file= open("sample.txt",encoding="utf-8")

for line in file:
    line = line.rstrip()
    print(line)

file.close()