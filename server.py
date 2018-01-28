#importing library for the server
from flask import Flask, flash, redirect, render_template, request, session, abort

#importing matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

app = Flask(__name__, template_folder='html')

#getting the home page
@app.route('/')
def home():
	return render_template('index.html')

#getting the youtube link
@app.route('/youtube', methods=['POST'])
def getYoutube():
	path = request.form['link']
	if "www.youtube.com" not in path:
		path = "https://www.youtube.com/watch?v="

if __name__ == "__main__":
	app.run(debug=True)