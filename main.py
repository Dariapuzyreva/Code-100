from flask import *
from data import db_session
from data.users import Users
from flask_sqlalchemy import SQLAlchemy
from jinja2 import *
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
# app.config['SECRET_KEY'] = 'sdf87krefsdaqwf485egr12gr'


menu = [{'name': 'Главная', 'url': '/'},
        {'name': 'Теория', 'url': 'theory'},
        {'name': 'Тренажер', 'url': 'exerciser'},
        {'name': 'О нас', 'url': 'about'},
        {'name': 'Личный кабинет', 'url': 'login'}]


@app.route('/')
def main():
    return render_template('index1.html', menu=menu)


@app.route('/theory')
def theory():
    return render_template('theory.html', menu=menu)


@app.route('/exerciser')
def variants():
    return render_template('exerciser.html', menu=menu)


@app.route('/about')
def about_us():
    return render_template('about_us.html', menu=menu)


@app.route('/login', methods=['POST', 'GET'])
def login():
    message = ''
    # if request.method == 'POST':
    #     try:
    #         hash = generate_password_hash(request.form['password'])
    #     except:
    #         pass

    #     if '@' not in request.form['email']:
    #         flash('error')
    #     else:
    #         flash('g')
    # if 'logged' in session:

    print(request.form['email'])
    return render_template('login.html', menu=menu, message=message)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html', title='Страница не найдена', menu=menu), 404


if __name__ == '__main__':
    db_session.global_init('db/users.sqlite')
    db_session.global_init('db/achievements.sqlite')
    app.run(port=4000)
    session.clear()
