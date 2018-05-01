from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
import re

table = open("playlist.html")
bs = BeautifulSoup(table.read(), "html.parser")
tds = [row.findAll('td') for row in bs.findAll('tr')]

TWiC_index = bs.body.h1.contents[0].split(' ')[2]

#.cue metadata
# TODO: Parse these from the MP3 or something
title = "Example Title"
file = "TWiC 192_ Example Filename.mp3"

tds.pop(0)
trackList = open('playlist.txt', 'w+')
trackCue = open(TWiC_index + '.cue', 'w+')
counter = 0

startTime = datetime.strptime(tds[0][0].string, '%Y/%m/%d %H:%M:%S')

#CUE File
trackCue.write("TITLE " + '"' + title + '"' + "\n")
trackCue.write("FILE " + '"' + file + '"' + "\n")

# Iterate through table rows
for td in tds:
	ts = (datetime.strptime(td[0].string, '%Y/%m/%d %H:%M:%S') - startTime)

	#trim '00:' from timestamp
	timeStamp = str(ts)[2:] if int(str(ts)[0]) < 1 else str(ts)

	trackArtist = td[1].string

	# Remove garbage from track name
	result = re.sub('([\w\d]+\/?)+(\s-\s)\d+$', '', td[2].string).rstrip(' -')
	if result:
		trackTitle = result
	else:
		trackTitle = td[2].string

	trackList.write(timeStamp + " - " + trackArtist.encode('utf-8') + " - " + trackTitle.encode('utf-8') + "\n")

	#create a datetime object by recovering the time from the timeStamp string
	#this lets us display the time in any format we want
	timeIndex = datetime.strptime(str(ts), '%H:%M:%S')

	if int(timeIndex.strftime('%H')) > 0:
		timeIndex_str = timeIndex.strftime('%H:%M:%S') + ':00'
	else:
		timeIndex_str = timeIndex.strftime('%M:%S') + ':00'

	counter += 1
	trackCue.write("TRACK " + str('%02d' % counter) + " AUDIO\n")
	trackCue.write("\tTITLE " + '"' + trackTitle.encode('utf-8') + '"' + '\n')
	trackCue.write("\tINDEX " + '01' + ' ' + timeIndex_str + '\n')