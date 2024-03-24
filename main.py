import flask
from flask import url_for, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('id', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

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

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return flask.render_template('login.html', title="Login", form=form)

@app.route('/destribution')
def destribution():
    names = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур",
             "Тедди Сандерс", "Шон Бин"]
    return flask.render_template('cabins.html', title="Destribution", astronauts=names)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

