import csv
lanternfish = []
with open ('test.txt', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		for i in row:
			lanternfish.append(int(i))

numoffish = (len(lanternfish))

for x in range(0,80):
	for i in range(len(lanternfish)):
		if lanternfish[i] == 0:
			lanternfish[i] = 6
			lanternfish.append(8)
		else:
			lanternfish[i] -= 1
	print(len(lanternfish))
