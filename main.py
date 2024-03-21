import flask
from flask import url_for

app = flask.Flask(__name__)

@app.route('/')
@app.route('/index/<string:title>')
def index(title=''):
    return flask.render_template('base.html', title=title)

@app.route('/list_prof/<string:list>')
def prof(list='ol'):
    return flask.render_template('prof.html', list=list)

@app.route('/answer')
@app.route('/auto_answer')
def answer():
    ans = ['Watny', 'Mark', 'выше среднего', 'штурман марсохода', 'male', 'всегда мечтал застрять на Марсе!', True]
    answer = {'title': 'Ответы',
           'surname': ['Фамилия', ans[0]], 'name': ['Имя', ans[1]],
           'education': ['Образование', ans[2]], 'profession': ['Профессия', ans[3]],
           'sex': ['Пол', ans[4]], 'motivation': ['Мотивация', ans[5]],
           'ready' : ['Готовы остаться на Марсе?', ans[6]]}
    return flask.render_template('auto_answer.html', answer=answer)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

