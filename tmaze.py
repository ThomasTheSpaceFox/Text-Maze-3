#!/usr/bin/env python
# coding=utf-8
# Tmaze

#mazemod = m.read()
mazemodpath = ('./MAZE/sample.MOD.txt')
mazefilepath = ('./MAZE/sample.MAZE')
#print (mazemod)
#print (mazefile)
#print(m.read())
print ("loading data from:" + mazefilepath)
n = open(mazefilepath)
datacnt = 1
for datalst in n:
	if datacnt==1:
		mazetitle = datalst.replace("\n", "")
		print ("maze title:" + datalst.replace("\n", ""))
	if datacnt==2:
		mazemodpath = ("./MAZE/" + datalst.replace("\n", ""))
		print ('.MOD.txt file: \n' + "./MAZE/" + datalst.replace("\n", ""))
	if datacnt==3:
		mazesizey = datalst.replace("\n", "")
		print ("maze size y:" + datalst.replace("\n", ""))
	if datacnt==4:
		mazesizex = (datalst).replace("\n", "")
		print ('maze size x:' + datalst.replace("\n", ""))
	if datacnt==5:
		playerstarty = (datalst.replace("\n", ""))
		print ('player start y:' + datalst.replace("\n", ""))
	if datacnt==6:
		playerstartx = (datalst.replace("\n", ""))
		print ('player start x:' + datalst.replace("\n", ""))
	if datacnt==7:
		endposy = (datalst.replace("\n", ""))
		print ('end pos y:' + datalst.replace("\n", ""))
	if datacnt==8:
		endposx = (datalst.replace("\n", ""))
		print ('end pos x:' + datalst.replace("\n", ""))
	datacnt += 1
n.close()
print ("data loaded. \n")


def lookpoint(lookptx, lookpty):
	lineycnt=1
	linexcnt=1
	m = open(mazemodpath)
	for lineylst in m:
		if lineycnt==lookpty:
			for linexlst in lineylst:
				if linexcnt==lookptx:
					return (linexlst)
				linexcnt += 1
		lineycnt += 1


if lookpoint(2, 2)==('0'):
	print ('blah')
print (lookpoint(2, 2))


