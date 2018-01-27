#importing library for the server
from flask import Flask 

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__, template_folder='html')

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

@app.route('/')
def home():
	return render_template('index.html')

if __name__ == "__main__":
	app.run()