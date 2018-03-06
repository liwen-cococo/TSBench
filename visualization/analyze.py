import StringIO
from flask import Flask, Blueprint, render_template, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from tsbench.scoring import addTogether
from tsbench.helper import getSingleData

analyze = Blueprint('analyze', __name__)

@analyze.route('/data/<dir_name>/<file_name>')
def plotFile(dir_name, file_name):
    return render_template('details.html', text='/text/'+dir_name+'/'+file_name, png='/png/'+dir_name+'/'+file_name)

@analyze.route('/text/<dir_name>/<file_name>')
def text(dir_name, file_name):
    return 'TO DO: illustration about this file'

@analyze.route('/png/<dir_name>/<file_name>')
def png(dir_name, file_name):
    file_path = './data/' + dir_name + '/' + file_name
    fig = Figure(figsize=(13, 4), dpi=100)
    axis = fig.add_subplot(1, 1, 1)

    ys = getSingleData(file_path)
    xs = range(ys.__len__())
    axis.plot(xs, ys)

    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response
