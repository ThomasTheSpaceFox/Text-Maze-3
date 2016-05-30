#!/usr/bin/env python
# coding=utf-8
# Tmaze

mazemodpath = ('./MAZE/sample.MOD.txt')
mazefilepath = ('./MAZE/sample.MAZE')
##############
#wordbindings:
##############
#FORWARD
FORWARDWORDBIND=('forward')
#BACKWARD
BACKWARDWORDBIND=('back')
#left
LEFTWORDBIND=('left')
#right
RIGHTWODBIND=('right')
#quit
QUITWORDBIND=('quit')
##############


# *.MAZE file data loader
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
		mazesizey = int(datalst.replace("\n", ""))
		print ("maze size y:" + datalst.replace("\n", ""))
	if datacnt==4:
		mazesizex = int(datalst.replace("\n", ""))
		print ('maze size x:' + datalst.replace("\n", ""))
	if datacnt==5:
		playerstarty = int((datalst.replace("\n", "")))
		print ('player start y:' + datalst.replace("\n", ""))
	if datacnt==6:
		playerstartx = int((datalst.replace("\n", "")))
		print ('player start x:' + datalst.replace("\n", ""))
	if datacnt==7:
		endposy = int((datalst.replace("\n", "")))
		print ('end pos y:' + datalst.replace("\n", ""))
	if datacnt==8:
		endposx = int((datalst.replace("\n", "")))
		print ('end pos x:' + datalst.replace("\n", ""))
	datacnt += 1
n.close()
print ("data loaded. \n")
playx = playerstartx
playy = playerstarty
debugset = ('1')
gameend = ('0')
CANTMOVE = ("Can't move in that direction.")
WINGAME = ("You win!")



#datapoint lookup function. used to read data points from the .MOD.txt file.
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

#old test data
#if lookpoint(2, 2)==('0'):
#	print ('blah')
#print (lookpoint(2, 2))

#main loop
while gameend==('0'):
	#pre POV image detection variable set and calculation area
	#
	#FALLBACK NULL IMAGE. KEEP! 
	POVVIEW = ('./TCR/NULL.TCR')
	POVforwardx = playx
	POVforwardy = playy + 1
	POVbackx = playx
	POVbacky = playy - 1
	POVleftx = playx + 1
	POVlefty = playy
	POVrightx = playx - 1
	POVrighty = playy
	FORWARD = lookpoint(POVforwardx, POVforwardy)
	BACKWARD = lookpoint(POVbackx, POVbacky)
	LEFTWARD = lookpoint(POVleftx, POVlefty)
	RIGHTWARD = lookpoint(POVrightx, POVrighty)
	if debugset==('1'):
		print ("F:" + FORWARD + "B:" + BACKWARD)
		print ("L:" + LEFTWARD + "R:" + RIGHTWARD)
	#gameend = ('1') #REMEMBER TO REMOVE THIS ONCE MAIN LOOP IS FUNCTIONAL
	#POV image selection.
	if (FORWARD==('0') and LEFTWARD==('1') and RIGHTWARD==('1') and BACKWARD==('0')):
		POVVIEW = ('./TCR/MAZE0.TCR')
	if (FORWARD==('1') and LEFTWARD==('1') and RIGHTWARD==('1') and BACKWARD==('0')):
		POVVIEW = ('./TCR/MAZE1.TCR')
	if (FORWARD==('1') and LEFTWARD==('1') and RIGHTWARD==('0') and BACKWARD==('0')):
		POVVIEW = ('./TCR/MAZE2.TCR')
	if (FORWARD==('1') and LEFTWARD==('0') and RIGHTWARD==('0') and BACKWARD==('0')):
		POVVIEW = ('./TCR/MAZE3.TCR')
	if (FORWARD==('1') and LEFTWARD==('0') and RIGHTWARD==('1') and BACKWARD==('0')):
		POVVIEW = ('./TCR/MAZE4.TCR')
	if (FORWARD==('0') and LEFTWARD==('0') and RIGHTWARD==('1') and BACKWARD==('0')):
		POVVIEW = ('./TCR/MAZE5.TCR')
	if (FORWARD==('0') and LEFTWARD==('1') and RIGHTWARD==('0') and BACKWARD==('0')):
		POVVIEW = ('./TCR/MAZE6.TCR')
	if (FORWARD==('0') and LEFTWARD==('0') and RIGHTWARD==('0') and BACKWARD==('0')):
		POVVIEW = ('./TCR/MAZE7.TCR')
	if (FORWARD==('1') and LEFTWARD==('0') and RIGHTWARD==('0') and BACKWARD==('1')):
		POVVIEW = ('./TCR/MAZE8.TCR')
	if (FORWARD==('0') and LEFTWARD==('0') and RIGHTWARD==('1') and BACKWARD==('1')):
		POVVIEW = ('./TCR/MAZE9.TCR')
	if (FORWARD==('0') and LEFTWARD==('1') and RIGHTWARD==('0') and BACKWARD==('1')):
		POVVIEW = ('./TCR/MAZEA.TCR')
	if (FORWARD==('0') and LEFTWARD==('0') and RIGHTWARD==('0') and BACKWARD==('1')):
		POVVIEW = ('./TCR/MAZEB.TCR')
	if (FORWARD==('1') and LEFTWARD==('1') and RIGHTWARD==('0') and BACKWARD==('1')):
		POVVIEW = ('./TCR/MAZEC.TCR')
	if (FORWARD==('1') and LEFTWARD==('0') and RIGHTWARD==('1') and BACKWARD==('1')):
		POVVIEW = ('./TCR/MAZED.TCR')
	if (FORWARD==('0') and LEFTWARD==('1') and RIGHTWARD==('1') and BACKWARD==('1')):
		POVVIEW = ('./TCR/MAZEE.TCR')
	#draw selected POV image
	i = open(POVVIEW)
	POVTCR = i.read()
	print (POVTCR)
	i.close()
	usrentry = ('null')
	#user prompt loop
	while (usrentry!=FORWARDWORDBIND and usrentry!=BACKWARDWORDBIND and usrentry!=LEFTWORDBIND and usrentry!=RIGHTWODBIND and usrentry!=QUITWORDBIND):
		print ("forward:" + FORWARDWORDBIND + " | backward:" + BACKWARDWORDBIND)
		print ("left:" + LEFTWORDBIND + " | right:" + RIGHTWODBIND + " | quit:" + QUITWORDBIND)
		usrentry = raw_input(':')
	print (chr(27) + "[2J" + chr(27) + "[H")
	#wall detection logic
	if usrentry==BACKWARDWORDBIND:
		BIND1 = playy - 1
		if lookpoint(playx, BIND1)==('1'):
			print (CANTMOVE)
		elif lookpoint(playx, BIND1)==('0'):
			playy -= 1
	if usrentry==FORWARDWORDBIND:
		BIND2 = playy + 1
		if lookpoint(playx, BIND2)==('1'):
			print (CANTMOVE)
		elif lookpoint(playx, BIND2)==('0'):
			playy += 1
	if usrentry==LEFTWORDBIND:
		BIND4 = playx + 1
		if lookpoint(BIND4, playy)==('1'):
			print (CANTMOVE)
		elif lookpoint(BIND4, playy)==('0'):
			playx += 1
	if usrentry==RIGHTWODBIND:
		BIND3 = playx - 1
		if lookpoint(BIND3, playy)==('1'):
			print (CANTMOVE)
		elif lookpoint(BIND3, playy)==('0'):
			playx -= 1
	#misic user commands
	if usrentry==QUITWORDBIND:
		gameend=('1')
	#game win check
	if (playx==endposx and playy==endposy):
		print(WINGAME)
		gameend=('1')

