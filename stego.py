from PIL import Image
import random


def encode(img, save):
	im = Image.open(img)
	pixels = im.load()

	print "Enter Secret: "
	secret = raw_input()
	secretenc = []
	for char in secret:
	    secretenc.insert(0,ord(char))

	if len(secretenc) > 255:
		print "The secret is too long!"
		exit()
	print secretenc
	loc1 = random.randrange(0,255,1)
	loc2 = random.randrange(0,255,1)
	#print loc1
	#print loc2

	first = len(secretenc), loc1, loc2

	print pixels[0,0]
	pixels[0,0] = first

	counter = 0
	for letter in secretenc:
		curpixel = pixels[loc1,loc2]
		newpixel = secretenc[counter],curpixel[1],curpixel[2]
		pixels[loc1,loc2] = newpixel
		loc1 = loc1 + 1
		loc2 = loc2 + 1
		counter = counter + 1

	print pixels[0,0]

	im.save(save, "PNG", quality=100, optimize=True, progressive=True)

def decode(img):
	newim = Image.open(img)
	newpixels = newim.load()
	firstpix = newpixels[0,0]
	secretlength = firstpix[0]

	loc1 = firstpix[1]
	loc2 = firstpix[2]

	counter = 0
	string = []
	while counter < secretlength:
		curpixel = newpixels[loc1,loc2]
		string.append(curpixel[0])
		loc1 = loc1 + 1
		loc2 = loc2 + 1
		counter = counter + 1
	newstring = []
	for char in string:
		newstring.insert(0,str(unichr(char)))
	print "".join(newstring)


encode("E:\\Google Drive\\School\\College\\Year 4\\AntiForensics\\pic.jpg", "E:\\Google Drive\\School\\College\\Year 4\\AntiForensics\\out.jpg")
decode("E:\\Google Drive\\School\\College\\Year 4\\AntiForensics\\out.jpg")