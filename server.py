#importing library for the server
from flask import Flask 

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello world!"

if __name__ == "__main__":
	app.run()