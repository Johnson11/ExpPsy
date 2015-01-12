import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr   


wert = [75,86,99,101,147,148.2,178.2]
labels = ["Farm","Boot","Brettspiel","Galerie","Videospiel","Palestinenserin","Hase"]
means = [8.64,5.47,12.42,10.10,10.05,13.25,32.46]

plt.figure()
images = [0,1,2,3,4,5,6]
for im in images:
	plt.plot(wert[im],means[im],'x',label=labels[im])
plt.legend(loc=2)
plt.ylabel("Average Response Time in s")
plt.xlabel("Difficulty Factor")
print "Result Person Correlation: ",pearsonr(wert,means)
fit = np.polyfit(wert,means,1)
fit_fn = np.poly1d(fit)
print "Function: ",fit_fn
plt.plot(wert,fit_fn(wert),'--r')

plt.show()
