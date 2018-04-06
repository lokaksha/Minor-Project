from PIL import Image

im=Image.open("transpose.png")
pix=im.load()

w=im.size[0]
h=im.size[1]

file=open("k.txt","r")
for x in file:
	k=int(x)

x=[]
for i in range(w):
	y=[]
	for j in range(h):
		y.append([0,0,0])
	x.append(y)


for i in range(w):
	for j in range(h):
		x[i][j][0]=pix[(i+k)%w,j][0]
for i in range(w):
	for j in range(h):
		x[i][j][1]=pix[(i+k)%w,j][1]
for i in range(w):
	for j in range(h):
		x[i][j][2]=pix[(i+k)%w,j][2]

for i in range(w):
	for j in range(h):
		pix[i,j]=tuple(x[i][j])

for i in range(w):
	for j in range(h):
		x[i][j][0]=pix[i,(j+k)%h][0]
for i in range(w):
	for j in range(h):
		x[i][j][1]=pix[i,(j+k)%h][1]
for i in range(w):
	for j in range(h):
		x[i][j][2]=pix[i,(j+k)%h][2]

for i in range(w):
	for j in range(h):
		pix[i,j]=tuple(x[i][j])

im.save("original.png")
