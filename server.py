from flask import Flask, session, render_template, request, redirect, url_for
from models import Article, db
import os

app = Flask(__name__)  # creating the app
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db' #os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = os.environ.get("MAIL_SERVER")
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")

db.init_app(app)


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    SECRET_KEY = os.environ.get("SECRET_KEY")


# Dashboard namespace


@app.route("/")
def index():
    ''' Index route'''
    return render_template('index.html', Title='Home')


@app.route('/<string:category>')
def get_cat(category):
    '''category route'''
    print(category)
    return render_template('index.html', Title='category')


@app.route("/EZine")
def e_zine():
    '''Ezine from the front page'''
    return render_template("ezine.html", Title='ezine')

# admin namespace


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'username' in session:
        return redirect(url_for('admin'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get("password")
        if password == os.environ.get("USER_PASSWORD") and username == os.environ.get('USER_NAME'):
            session['username'] = username
            return redirect(url_for('admin'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index', Title='index'))


@app.route('/admin')
def admin():
    ''' admin gives a dashboard to work with'''
    return render_template('admin/admin.html', Title="admin")


@app.route('/admin/ezine', methods=['POST', 'GET'])
def admin_ezine():
    '''We can edit the ezine from here'''
    if request.method == "POST":
        subject = request.form.get('subject')
        body = request.form.get('body')
        if not subject == '' and not body == '':
            article = Article(subject,body)
            db.session.add(article)
            db.session.commit()
    return render_template('admin/ezine/ezine.html', Title='create zine')


@app.route('/admin/upload')
def admin_upload():
    ''' We can upload images from here'''
    return render_template('admin/upload/upload.html', Title='upload images')


# starting the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)

# We will change this during production and create
# a WSGI server to run it in a docker
# This server is intended to be the api to the EvertRobles website
# to provide it of the necessary data
# This development server can be started with 'py server.py'
# it will run on port 80 and will be reached globally from with you network

# create a flaskenv file to hold the following attributes
# DEBUG=True
# FLASK_ENV=development
# FLASK_APP=server.py
# APP_SETTINGS=FLASK_APP.configuration.config.DevelopmentConfig
# DATABASE_URL = '##############'
# USER_NAME = EAFlask
# USER_PASSWORD = ########
# SECRET_KEY= '#######'
# MAIL_SERVER='############'
# MAIL_PORT = 465
# MAIL_USE_TLS = False
# MAIL_USE_SSL = True
# MAIL_USERNAME = '###############'
# MAIL_PASSWORD = '##############'
# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_HTTPONLY = True
# SESSION_COOKIE_SAMESITE = 'None'
# CSRF_ENABLED = True
