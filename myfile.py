f = open("students")

mylines = f.readlines()

modified_lines = []
for item in mylines:
    a = item.strip("\n")
    modified_lines.append(a.upper())

print(modified_lines)

fw = open("mywork.txt", "w")
for item in modified_lines:
    fw.write(item+"\n")
fw.close()