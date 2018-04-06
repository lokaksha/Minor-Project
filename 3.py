from PIL import Image

im1=Image.open("chaos1.png")
pix1=im1.load()

im2=Image.open("chaos2.png")
pix2=im2.load()

w1=im1.size[0]
h1=im1.size[1]

w2=im2.size[0]
h2=im2.size[1]

file=open("k1.txt","r")
for x in file:
	k1=int(x)

file=open("k2.txt","r")
for x in file:
	k2=int(x)

file=open("k3.txt","r")
for x in file:
	k3=int(x)

x=[]
for i in range(w1):
	y=[]
	for j in range(h1):
		y.append([0,0,0])
	x.append(y)

for i in range(w1):
	for j in range(h1):
		x[i][j][0]=pix1[(i+k1)%w1,j][0]
for i in range(w1):
	for j in range(h1):
		x[i][j][1]=pix1[(i+k2)%w1,j][1]
for i in range(w1):
	for j in range(h1):
		x[i][j][2]=pix1[(i+k3)%w1,j][2]

for i in range(w1):
	for j in range(h1):
		pix1[i,j]=tuple(x[i][j])

for i in range(w1):
	for j in range(h1):
		x[i][j][0]=pix1[i,(j+k1)%h1][0]
for i in range(w1):
	for j in range(h1):
		x[i][j][1]=pix1[i,(j+k2)%h1][1]
for i in range(w1):
	for j in range(h1):
		x[i][j][2]=pix1[i,(j+k3)%h1][2]

for i in range(w1):
	for j in range(h1):
		pix1[i,j]=tuple(x[i][j])

im1.save("pre_final1.png")

x=[]
for i in range(w2):
	y=[]
	for j in range(h2):
		y.append([0,0,0])
	x.append(y)

for i in range(w2):
	for j in range(h2):
		x[i][j][0]=pix2[(i+k1)%w2,j][0]
for i in range(w2):
	for j in range(h2):
		x[i][j][1]=pix2[(i+k2)%w2,j][1]
for i in range(w2):
	for j in range(h2):
		x[i][j][2]=pix2[(i+k3)%w2,j][2]

for i in range(w2):
	for j in range(h2):
		pix2[i,j]=tuple(x[i][j])

for i in range(w2):
	for j in range(h2):
		x[i][j][0]=pix2[i,(j+k1)%h2][0]
for i in range(w2):
	for j in range(h2):
		x[i][j][1]=pix2[i,(j+k2)%h2][1]
for i in range(w2):
	for j in range(h2):
		x[i][j][2]=pix2[i,(j+k3)%h2][2]

for i in range(w2):
	for j in range(h2):
		pix2[i,j]=tuple(x[i][j])

im2.save("pre_final2.png")
