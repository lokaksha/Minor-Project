from PIL import Image
from random import randint

im=Image.open("secret.png")
pix=im.load()

w=im.size[0]
h=im.size[1]

k=randint(0,w)

with open("k.txt","w") as f:
	f.write(str(k))

x=[]
for i in range(w):
	y=[]
	for j in range(h):
		y.append([0,0,0])
	x.append(y)

for i in range(w):
	for j in range(h):
		x[i][(j+k)%h][0]=pix[i,j][0]
for i in range(w):
	for j in range(h):
		x[i][(j+k)%h][1]=pix[i,j][1]
for i in range(w):
	for j in range(h):
		x[i][(j+k)%h][2]=pix[i,j][2]

for i in range(w):
	for j in range(h):
		pix[i,j]=tuple(x[i][j])

for i in range(w):
	for j in range(h):
		x[(i+k)%w][j][0]=pix[i,j][0]
for i in range(w):
	for j in range(h):
		x[(i+k)%w][j][1]=pix[i,j][1]
for i in range(w):
	for j in range(h):
		x[(i+k)%w][j][2]=pix[i,j][2]

for i in range(w):
	for j in range(h):
		pix[i,j]=tuple(x[i][j])

im.save("transpose.png")