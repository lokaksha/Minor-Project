from PIL import Image
from random import randint

im=Image.open("secret.png")
pix=im.load()

w=im.size[0]
h=im.size[1]

k1=[]
k2=[]
k3=[]

for i in range(w):
	temp=[]
	for j in range(h):
		temp.append(randint(0,2000))
	k1.append(temp)

for i in range(w):
	temp=[]
	for j in range(h):
		temp.append(randint(0,2000))
	k2.append(temp)

for i in range(w):
	temp=[]
	for j in range(h):
		temp.append(randint(0,2000))
	k3.append(temp)

# with open("k1.txt","w") as f:
# 	for i in range(w):
# 		for j in range(h):
# 			f.write(str(k1[i][j])+" ")
# 		f.write("\n")

# with open("k2.txt","w") as f:
# 	for i in range(w):
# 		for j in range(h):
# 			f.write(str(k2[i][j])+" ")
# 		f.write("\n")

# with open("k3.txt","w") as f:
# 	for i in range(w):
# 		for j in range(h):
# 			f.write(str(k3[i][j])+" ")
# 		f.write("\n")

x=[]
for i in range(w):
	y=[]
	for j in range(h):
		y.append([0,0,0])
	x.append(y)

for i in range(w):
	for j in range(h):
		x[i][(j+k1[i][j])%h][0]=pix[i,j][0]
for i in range(w):
	for j in range(h):
		x[i][(j+k2[i][j])%h][1]=pix[i,j][1]
for i in range(w):
	for j in range(h):
		x[i][(j+k3[i][j])%h][2]=pix[i,j][2]

for i in range(w):
	for j in range(h):
		pix[i,j]=tuple(x[i][j])

for i in range(w):
	for j in range(h):
		x[(i+k1[i][j])%w][j][0]=pix[i,j][0]
for i in range(w):
	for j in range(h):
		x[(i+k2[i][j])%w][j][1]=pix[i,j][1]
for i in range(w):
	for j in range(h):
		x[(i+k3[i][j])%w][j][2]=pix[i,j][2]

for i in range(w):
	for j in range(h):
		pix[i,j]=tuple(x[i][j])

im.save("confusion.png")