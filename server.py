#importing library for the server
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, Markup
#importing youtube mp3 converter
from mp3_youtube import *
#importing analyze function
from ibmWatson import *
#importing random
import random
#importing dictioanry
from Dictionary import *


app = Flask(__name__, template_folder='html', static_url_path='/static')

showing_image = "/static/histogram.png"
success_image = "/static/output.png"
failing_image = "/static/notfound.png"

styles = ["success", "danger", "info", "warning", "active"]

#getting the home page
@app.route('/', methods=['GET'])
def home():
	return render_template('index.html', image=showing_image, words="")

#getting the youtube link
@app.route('/', methods=['POST'])
def youtube():
	if request.method == 'POST':
		path = request.form['url']
		if "www.youtube.com" not in path:
			path = "https://www.youtube.com/watch?v=" + path

		sending_image = success_image

		#temp data
		objArray = ['', '', '']
		tag_value = ""
		#if successfully download the mp3
		if download_mp3(path):
			analysis_success, objDict = waveToFreqsDict(3, "/sound.mp3", "./temp")
			if analysis_success:
				print(objDict)
				getFreqPlot(objDict, "./static/output.png")
				objArray = list()
				for i in objDict.keys():
					objArray.append(i)

				html_tag = ""
				for i in range(len(objArray)):
					meaning = get_meaning(objArray[i])
					html_tag += '<tr class="' + random.choice(styles) + '"><td>' + objArray[i] + '</td><td>'+meaning+'</td></tr>'
				
				tag_value = Markup(html_tag)

			else:
				sending_image = failing_image

		#if fail to download mp3
		else:
			sending_image = failing_image
		
		return render_template("index.html", result=path, image=sending_image, words=tag_value)


#for not caching the images
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == "__main__":
	app.run(debug=True)