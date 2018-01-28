from __future__ import unicode_literals
import youtube_dl

def supported(url):
    ies = youtube_dl.extractor.gen_extractors()
    for ie in ies:
        if ie.suitable(url) and ie.IE_NAME != 'generic':
            # Site has dedicated extractor
            return True
    return False

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

    if not supported(url):
        return False

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return True

