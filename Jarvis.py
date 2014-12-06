#!/usr/bin/python

import speech_recognition as sr
from subprocess import call

# Listen for data
def data_listen(r, dur):
	print "[REC] Listening for %d secs" % (dur)
	with sr.Microphone() as source:                # use the default microphone
            audio = r.listen(source, dur)

	print "[REC] Data recorded "
	return audio

def data_decode(r, data):
	text = r.recognize(data)
    
	return text



#############
# INIT
# cs-CZ en-US
r = sr.Recognizer("en-US", "AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")
r.energy_threshold = 2000
r.pause_threshold = 0.5

while (1):
	data = data_listen(r, 0)
	print "Got input ... going to recognizeo"
	try:
		text = data_decode(r, data)
	except LookupError:                            # speech is unintelligible
		print "Could not understand audio"
		continue
	print "Recognized - " + text
	if "radio" in text:
        #		call(["/Applications/VLC.app/Contents/MacOS/VLC", "-I dummy","http://pool.cdn.lagardere.cz/dance-radio128.mp3"])
		call(["vlc", "-I dummy","http://ice.abradio.cz/beat128.mp3"])

