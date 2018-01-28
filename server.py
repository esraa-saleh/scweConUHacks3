#importing library for the server
from flask import Flask, flash, redirect, render_template, request, session, abort
#importing youtube mp3 converter
from mp3_youtube import *

app = Flask(__name__, template_folder='html')

#getting the home page
@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')

#getting the youtube link
@app.route('/', methods=['POST'])
def youtube():
	if request.method == 'POST':
		path = request.form['url']
		if "www.youtube.com" not in path:
			path = "https://www.youtube.com/watch?v=" + path
		print(path)

		download_mp3(path)
		
		return render_template("index.html", result=path)
	#path = request.form['url']
	#if "www.youtube.com" not in path:
	#	path = "https://www.youtube.com/watch?v="

if __name__ == "__main__":
	app.run(debug=True)