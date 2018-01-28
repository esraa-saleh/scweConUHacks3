#importing library for the server
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
#importing youtube mp3 converter
from mp3_youtube import *

app = Flask(__name__, template_folder='html', static_url_path='/static')

showing_image = "/static/histogram.png"
testing_image = "/static/testing.png"
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
		print(path)

		if download_mp3(path):
			sending_image = testing_image
		else:
			sending_image = failing_image
		
		return render_template("index.html", result=path, image=sending_image)
	#path = request.form['url']
	#if "www.youtube.com" not in path:
	#	path = "https://www.youtube.com/watch?v="

if __name__ == "__main__":
	app.run(debug=True)