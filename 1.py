from PIL import Image

def fullb(s):
	n=len(s)
	for i in range(n,8):
		s="0"+s
	return s

im=Image.open("secret.png")
im1=Image.open("cover1.png")
im2=Image.open("cover2.png")
pix=im.load()
pix1=im1.load()
pix2=im2.load()

print im.size
print im1.size
print im2.size

for i in range(im.size[0]):
	for j in range(im.size[1]):
		x=[]
		for m in pix[i,j]:
			x.append(fullb("{0:b}".format(m)))
		y=[]
		for m in pix1[i,j]:
			y.append(fullb("{0:b}".format(m)))
		z=[]
		for m in pix2[i,j]:
			z.append(fullb("{0:b}".format(m)))

		temp1=[]
		for m in range(3):
			temp1.append(int(y[m][:4]+x[m][:4],2))

		temp2=[]
		for m in range(3):
			temp2.append(int(z[m][:4]+x[m][4:],2))

		pix1[i,j]=tuple(temp1)
		pix2[i,j]=tuple(temp2)

im1.save("steg1.png")
im2.save("steg2.png")
