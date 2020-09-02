file= open("sample.txt",encoding="utf-8")

counter = 0

for line in file:
    counter += 1
    line = line.strip()
    print(str(counter)+':'+ line)

file.close()