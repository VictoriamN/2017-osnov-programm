import sys

lines = sys.stdin.readlines()

for line in lines:
	s = line.replace(".",".\n")
	print(s)
