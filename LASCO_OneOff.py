from sunpy.net.helioviewer import HelioviewerClient
import matplotlib.pyplot as plt
from matplotlib.image import imread
from PIL import Image

import subprocess
import datetime

def get_date():
	year = int(raw_input("YEAR: ").zfill(4))
	month = int(raw_input("MONTH: ").zfill(2))
	day = int(raw_input("DAY: ").zfill(2))

	return year, month, day

def build_timelist(YEAR, MONTH, DAY):
	times = []

	for hours in range (0, 24):
		for minutes in xrange (0, 60, 12):
			times.append(datetime.datetime(YEAR, MONTH, DAY, hours, minutes, 00))
	return times


if __name__ == '__main__':
	
	year, month, day = get_date()

	timelist = build_timelist(year, month, day)
	hv = HelioviewerClient()  
	#file = hv.download_png('2015/01/01', 6, "[SDO,AIA,AIA,304,1,100],[SDO,AIA,AIA,193,1,50],[SOHO,LASCO,C2,white-light,1,100],[SOHO,LASCO,C3,white-light,1,100]", x0=0, y0=0, width=900, height=900)  
	minutes = []
	for minute in xrange(0, 60, 12):
		minutes.append(minute)

	for time in timelist:
		filenum = timelist.index(time) + 1
		total = len(timelist)
		print("DOWNLOADING: " + str(time) + " --- " + str(filenum) + "/" + str(total))
		file = hv.download_png(time, 6, 
		                       "[SDO,AIA,AIA,193,1,100],"\
		                       "[SOHO,LASCO,C2,white-light,1,100]",
		                       directory="./downloaded", 
		                       x0=0, y0=0, width=2000, height=2000, watermark=False)  



# print("TIMELIST: ", timelist)
# subprocess.call("cp " + str(file).split('u/') + " from_hl.png")

# im = imread(file)
# print("IM: ", im)  
# plt.imshow(im)

# plt.axis('off')  
# plt.savefig("test.png", edgecolor='b', bbox_inches="tight", pad_inches=0)
# plt.show()  