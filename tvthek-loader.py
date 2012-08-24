import requests
import re
import sys
import os
from BeautifulSoup import BeautifulSoup

def rtmpString (stream, show):
	return ('rtmpdump -r "rtmp://apasfw.apa.at/cms-worldwide/" -a "cms-worldwide/" -f "WIN 11,1,102,55" -W "http://tvthek.orf.at/flash/player/TVThekPlayer_9_ver18_1.swf" -p "'+ show +'" -y "'+ stream +'" -v -o ' + output)

showlink = sys.argv[1]
output = sys.argv[2]

r = requests.get('http://tvthek.orf.at/programs/4492845-Mein-Simmering/episodes/4482181-Mein-Simmering/4493119-Mein-Simmering')

soup = BeautifulSoup(r.text)

for elem in soup('script', text=re.compile(r'ORF\.jsVideoPlayer')):
	playerCode = elem.parent

playerCodeString = playerCode.contents

for item in playerCodeString:
	m = re.search('mp4\:([^:]*?)mp4',item)

streamlink = m.group(0)

os.system(rtmpString(streamlink,showlink))

