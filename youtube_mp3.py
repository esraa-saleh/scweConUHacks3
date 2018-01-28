from subprocess import call
import os

import ssl
from pytube import YouTube

#disable the ssl verification
try:
 	_create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
	pass
else:
	ssl._create_default_https_context = _create_unverified_https_context

#set up url
URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

yt = YouTube(URL)

#getting the first video
vid = yt.streams.first()

#download the video first
vid.download()

title = vid.default_filename   
output = "./temp/output.mp3"

#converting by ffmpeg
call(["ffmpeg", "-i", title, output])

#deleting the mp4
os.remove(title)