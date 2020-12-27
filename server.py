from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)  # creating the app


class Config(object):
    DEBUG = False
    TESTING = False
    # CSRF_ENABLED = True
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # TWITTER_OAUTH_CLIENT_KEY = os.environ.get("TWITTER_OAUTH_CLIENT_KEY")
    # TWITTER_OAUTH_CLIENT_SECRET = os.environ.get("TWITTER_OAUTH_CLIENT_SECRET")
    # SESSION_COOKIE_SECURE = True
    # SESSION_COOKIE_HTTPONLY = True
    # SESSION_COOKIE_SAMESITE = 'None'
    # MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = 465
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    SECRET_KEY = "secret_for_test_environment"


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
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get("password")
        if password == os.environ.get("USER_PASSWORD") and username == os.environ.get('USER_NAME'):
            return redirect(url_for('admin'))
    return render_template('login.html')


@app.route('/admin')
def admin():
    ''' admin gives a dashboard to work with'''
    return render_template('admin/admin.html', Title="admin")


@app.route('/admin/ezine')
def admin_ezine():
    '''We can edit the ezine from here'''
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
