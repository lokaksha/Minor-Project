from PIL import Image

def fullb(s):
	n=len(s)
	for i in range(n,8):
		s="0"+s
	return s

im1=Image.open("pre_final1.png")
im2=Image.open("pre_final2.png")
pix1=im1.load()
pix2=im2.load()

for i in range(im1.size[0]):
	for j in range(im1.size[1]):
		x=[]
		for m in pix1[i,j]:
			x.append(fullb("{0:b}".format(m)))

		y=[]
		for m in pix2[i,j]:
			y.append(fullb("{0:b}".format(m)))
			
		temp=[]
		for m in range(3):
			temp.append(int(x[m][4:]+y[m][4:],2))
		pix1[i,j]=tuple(temp)

im1.save("Final.png")