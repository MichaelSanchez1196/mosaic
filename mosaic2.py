from PIL import Image
from collections import Counter 
#for the image open(line 3), make sure we include our path for the image in our computer
im = Image.open("/home/michael/Documents/spring16/cst205/project2/MarleySoccer.jpg")
#im.show()

redPixelList = []
greenPixelList = []
bluePixelList = []

#finds the width and height of the image.
width, height = im.size
#print width
#print height

tileHeight = height /3
tileWidth = width

beginWidth = 0
beginHeight = 0



finalImg = Image.new("RGB",(width,height),"Black")

#finalImg.show()

		#rgb_im = im.convert('RGB')
		#r, g, b = rgb_im.getpixel((xPos, yPos))
"""
for times in range(0,3):
	for xPos in range(beginWidth,tileWidth):
		for yPos in range(beginHeight,tileHeight):

		#pixel = getPixel(im,xPos,yPos)
		
			rgb_im = im.convert('RGB')
			r,g,b, = rgb_im.getpixel((xPos,yPos))

	    	redPixelList.append(r)
	    	greenPixelList.append(g)
	    	bluePixelList.append(b)
		

	#newPixel = getPixel(finalImg,xPos,yPos)
	
		mostRed = Counter(redPixelList)
		mostGreen = Counter(greenPixelList)
		mostBlue = Counter(bluePixelList)



		myRed = max(mostRed.values())
		modeRed = [k for k, v in mostRed.items() if v == myRed]
		myGreen = max(mostGreen.values())
		modeGreen = [k for k, v in mostGreen.items() if v == myGreen]
		myBlue = max(mostBlue.values())
		modeBlue = [k for k, v in mostBlue.items() if v == myBlue]



	print modeRed[0]
	print modeGreen[0]
	print modeBlue[0]
   
	del redPixelList[:]
	del greenPixelList[:]
	del bluePixelList[:]

	for imgX in range(beginWidth,tileWidth):
		for imgY in range(beginHeight,tileHeight):
			finalImg.putpixel((imgX,imgY),(modeRed[0],modeGreen[0],modeBlue[0]))

	if(times < 1):
		beginHeight += tileHeight
		beginWidth = 0
		tileHeight += tileHeight
	else :
		tileHeight += beginHeight
		beginHeight += beginHeight
		beginWidth = 0

	#grabing the modes of every tile	
	if(times == 0):
		firstRedMode = modeRed[0]
		firstGreenMode = modeGreen[0]
		firstBlueMode = modeBlue[0]
	elif(times == 1):
		secondRedMode = modeRed[0]
		secondGreenMode = modeGreen[0]
		secondBlueMode = modeBlue[0]
	else: 
		thirdRedMode = modeRed[0]
		thirdGreenMode = modeGreen[0]
		thirdBlueMode = modeBlue[0]

#finalImg.show()

#print firstRedMode,firstGreenMode,firstBlueMode
#print secondRedMode, secondGreenMode, secondBlueMode
#print thirdRedMode, thirdGreenMode, thirdBlueMode

#newIm.show()
"""

for bwX in range(0,height):
	for bwY in range(0,width):

		bw_im = im.convert("1")
		new_im = bw_im.convert("RGB")
		r,g,b = new_im.getpixel((bwX,bwY))
		
		if (r == 255 and bwX < (height / 3) ):
			print "First", bwX , bwY
			r,g,b = (144,153,0)
		elif(r == 255 and (bwX > height/3) and (bwX < (height/3) *2)):
			r,g,b = (165,172,131)
			print "second", bwX, bwY
		elif(r == 255 and bwX <= height): 
			r,g,b = (100,95,62)
			print "third", bwX, bwY

new_im.show()			
print("Image Displayed.")



