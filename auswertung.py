import numpy as np
import matplotlib.pyplot as plt
import csv 
import glob
import os

def read(Filename):
	cr = csv.reader(open(Filename,"rb"))
	for row in cr: 
		if row[6]!="im": #erste zeile ausschliessen
			im = int(row[6])
			if row[10]!="--":
				rt = float(row[10])
			else:
				rt = NOTHING
			#now weve read the variables
	
			images[im-1].append(rt)
			#now entered in images

NOTHING = 60.00

images = [[],[],[],[],[],[],[],[]]
img_title = ["Farm","Videospiel","Palestinerin","Testbild","Hase","Boot","Galerie","Brettspiel"]

os.chdir("/home/justin/Desktop/explab")
for file in glob.glob("*.csv"):
    read(file)

# now images stores at images[1] the images of picture 2 and so on...
plt.figure("Images and Time n = 13")
nr = 1
mean = []
median = []
std = []

for img_nr in images:
	plt.subplot(4,2,nr)
	plt.title(nr)
	plt.hist(img_nr)
	plt.xlabel("Time in seconds")
	plt.ylabel("Subjects")
	mean.append(np.mean(img_nr))
	median.append(np.median(img_nr))
	std.append(np.std(img_nr))
	print "Image Nr.",nr," Mean:",np.mean(img_nr)," Median:",np.median(img_nr),\
		" Std:",np.std(img_nr)
	nr = nr +1# increment the numbe

#now saving to one single csv
with open("outputCombined.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(images)

#plt.savefig("results-histogram.jpg")

plt.figure("Statistical Data of Images")

plt.boxplot(images)
plt.ylabel("Time in Seconds")
plt.xlabel("Image Nr.")
locs , _ = plt.xticks()
plt.xticks(locs,img_title,rotation=17)

#plt.savefig("results-boxplot.jpg")
plt.show()	




