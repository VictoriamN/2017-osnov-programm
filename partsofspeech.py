import sys

vocab =  sys.stdin.readlines()

table = {}

fd = open("annotated.txt")
for line in fd.readlines():
	line = line.strip("\n")
	if "\t" not in line:
		continue
	line = line.split("\t")
	inn = line[0]
	out = line[1]
	table[inn] = out

for b in vocab:
	b = b.strip()
	if b.count("\t") == 0:
		print(b)
		continue
	line = b.split("\t")
	surf = line[1]
	if surf in table:
		line[3] = table[surf]
	print("\t".join(line))