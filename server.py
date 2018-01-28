#importing library for the server
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
#importing youtube mp3 converter
from mp3_youtube import *
#importing analyze function
from ibmWatson import *

app = Flask(__name__, template_folder='html', static_url_path='/static')

showing_image = "/static/histogram.png"
success_image = "/static/output.png"
failing_image = "/static/notfound.png"

#getting the home page
@app.route('/', methods=['GET'])
def home():
	return render_template('index.html', image=showing_image)

#getting the youtube link
@app.route('/', methods=['POST'])
def youtube():
	if request.method == 'POST':
		path = request.form['url']
		if "www.youtube.com" not in path:
			path = "https://www.youtube.com/watch?v=" + path

		#if successfully download the mp3
		if download_mp3(path):
			analysis_success, objDict = waveToFreqsDict(5, "/sound.mp3", "./temp")
			if analysis_success:
				print(objDict)
				getFreqPlot(objDict, "./static/output.png")
				sending_image = success_image
			else:
				sending_image = failing_image

		#if fail to download mp3
		else:
			sending_image = failing_image
		
		return render_template("index.html", result=path, image=sending_image)
	#path = request.form['url']
	#if "www.youtube.com" not in path:
	#	path = "https://www.youtube.com/watch?v="

if __name__ == "__main__":
	app.run(debug=True)