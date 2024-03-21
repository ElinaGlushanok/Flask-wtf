import flask

app = flask.Flask(__name__)

@app.route('/')
@app.route('/index/<string:title>')
def index(title=''):
    return flask.render_template('base.html', title=title)

@app.route('/list_prof/<string:list>')
def prof(list='ol'):
    return flask.render_template('prof.html', list=list)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

