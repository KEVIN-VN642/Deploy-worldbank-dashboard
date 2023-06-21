from flask import Flask
import json, plotly
from flask import render_template
from charts.charts import return_figures
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():

    figures = return_figures()

    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html',
                           ids=ids,
                           figuresJSON=figuresJSON)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)