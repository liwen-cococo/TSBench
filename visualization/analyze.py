import StringIO
from flask import Flask, Blueprint, render_template, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from tsbench.scoring import addTogether
from tsbench.helper import getSingleData

analyze = Blueprint('analyze', __name__, template_folder='./templates')

@analyze.route('/<algo_name>/<scor_name>/data/<dir_name>/<file_name>/')
def plotFile(algo_name, scor_name, dir_name, file_name):
    return render_template('details.html', 
                            text='/text/'+algo_name+'/'+scor_name+'/'+dir_name+'/'+file_name, 
                            png_true='/png_true/'+algo_name+'/'+scor_name+'/'+dir_name+'/'+file_name,
                            png_detected='/png_detected/'+algo_name+'/'+scor_name+'/'+dir_name+'/'+file_name)

@analyze.route('/text/<algo_name>/<scor_name>/<dir_name>/<file_name>/')
def text(algo_name, scor_name, dir_name, file_name):
    return 'TO DO: illustration about this file'

@analyze.route('/png_true/<algo_name>/<scor_name>/<dir_name>/<file_name>/')
def png_true(algo_name, scor_name, dir_name, file_name):
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


@analyze.route('/png_detected/<algo_name>/<scor_name>/<dir_name>/<file_name>/')
def png_detected(algo_name, scor_name, dir_name, file_name):
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
