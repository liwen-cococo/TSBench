import StringIO
from flask import Flask, render_template, make_response, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from tsbench.scoring import addTogether
from tsbench.helper import getSingleData

app = Flask(__name__)
data_dict = addTogether('./results/random/score_old.json')

@app.route('/')
def index():
    message = """ 
    </br>
    <table align="center" border="1" width="600" frame="hsides" rules="groups" >
        <colgroup span="1" width="200"></colgroup>
        <colgroup span="6" width="600"></colgroup>
        <thead>
            <tr>
            <td></td>
            <td>TP</td>
            <td>FP</td>
            <td>FN</td>
            <td>Precision</td>
            <td>Recall</td>
            <td>F-Score</td>
            </tr>
        </thead>
        <tbody>
    """
    message += """<tr><td>total</td>"""
    for j in [0, 2, 3, 4, 5, 6]:
        message += """<td>""" + str(data_dict['total'][j]) + """</td>"""
    message += """</tr>"""

    for k in data_dict:
        if(k != 'total'):
            message += """<tr>"""
            message += """<td>""" + k + """</td>"""
            for j in [0, 2, 3, 4, 5, 6]:
                message += """<td>""" + str(data_dict[k][j]) + """</td>"""
            message += """</tr>"""
    message += """
        </tbody>
    </table>
    """

    return message


@app.route('/data/<dir_name>/<file_name>')
def plotFile(dir_name, file_name):
    return render_template('details.html', text='/text/'+dir_name+'/'+file_name, png='/png/'+dir_name+'/'+file_name)

@app.route('/text/<dir_name>/<file_name>')
def text(dir_name, file_name):
    return 'TO DO: illustration about this file'

@app.route('/png/<dir_name>/<file_name>')
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


if __name__ == '__main__':
    app.run(debug=True)
