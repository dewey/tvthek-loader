import requests
import re
import sys
import os
from BeautifulSoup import BeautifulSoup

def rtmpString (stream, show):
	return ('rtmpdump -r "rtmp://apasfw.apa.at/cms-worldwide/" -a "cms-worldwide/" -f "WIN 11,1,102,55" -W "http://tvthek.orf.at/flash/player/TVThekPlayer_9_ver18_1.swf" -p "'+ show +'" -y "'+ stream +'" -v -o ' + output + ".flv")

showlink = sys.argv[1]
output = sys.argv[2]
chapter = int(sys.argv[3])-1

r = requests.get(showlink)

soup = BeautifulSoup(r.text)

for elem in soup('script', text=re.compile(r'ORF\.jsVideoPlayer')):
	playerCode = elem.parent

playerCodeString = playerCode.contents

for item in playerCodeString:
	m = re.search('mp4\:([^:]*?)mp4',item)

streamlink = m.group(chapter)

os.system(rtmpString(streamlink,showlink))

