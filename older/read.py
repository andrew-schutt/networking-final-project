f = open('test.jpg', 'r')
lineList = []

while(True):
	temp = f.read(4)
	if temp == "":
		break

	lineList.append(temp)
	print temp



z = open('output','w')

for x in xrange(0,len(lineList)):
	z.write(lineList[x])