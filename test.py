import StringIO
from flask import Flask, render_template, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)
data_dict = addTogether('./results/random/score_old.json')

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)
