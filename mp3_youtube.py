from __future__ import unicode_literals
import youtube_dl

OK = 999
NOT_OK = 998

def download_mp3(url):
	ydl_opts = {
	    'format': 'bestaudio/best',
        'outtmpl': './temp/sound.%(ext)s',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3',
	        'preferredquality': '192',
	    }],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([url])

	return OK