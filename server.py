from flask import Flask, session, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from models import Article, Image, db
import os
from datetime import datetime

UPLOAD_FOLDER = '/-website/EAFlask/static/assets/img'

app = Flask(__name__)  # creating the app
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db' #os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = os.environ.get("MAIL_SERVER")
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024


db.init_app(app)


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    SECRET_KEY = os.environ.get("SECRET_KEY")


# index images
IMAGES = [
    {'url':"/static/assets/img/portfolio/sandex.jpg"},
    {'url':"/static/assets/img/portfolio/pathfinder.jpg"},
    {'url':"/static/assets/img/portfolio/metal-secrets.jpg"},
    {'url':"/static/assets/img/portfolio/synchonosity.jpg"},
    {'url':"/static/assets/img/portfolio/unfolding-evolution.jpg"},
    {'url':"/static/assets/img/portfolio/wheel-of-fortune.jpg"}
]
       
def allowed_image(filename):
    
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route("/")
def index():
    ''' Index route'''
    return render_template('index.html', Title='Home',images=IMAGES)


@app.route('/<string:category>')
def get_cat(category):
    '''category route'''
    print(category)
    return render_template('index.html', Title='category')


@app.route("/EZine")
def e_zine():
    '''Ezine from the front page'''
    articles = Article.query.all()
    return render_template("ezine.html", Title='ezine',articles=articles)

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
    return redirect(url_for('index'))


@app.route('/admin')
def admin():
    ''' admin gives a dashboard to work with'''
    if not 'username' in session:
        return redirect(url_for('login'))
    return render_template('admin/admin.html', Title="admin")


@app.route('/admin/ezine', methods=['POST', 'GET'])
def admin_ezine():
    '''We can edit the ezine from here'''
    if not 'username' in session:
        return redirect(url_for('login'))
    if request.method == "POST":
        subject = request.form.get('subject')
        body = request.form.get('body')       
        if not subject == '' and not body == '':
            article = Article(subject,body)
            db.session.add(article)
            db.session.commit()
    return render_template('admin/ezine/ezine.html', Title='create zine')


# we wil probably have to make a route where the owner can remove a certian file or image
@app.route('/admin/upload',methods=['POST','GET'])
def admin_upload():
    ''' We can upload images from here'''
    # You can only get here if you're properly authenticated
    if not 'username' in session:
        return redirect(url_for('login'))
    # Check to see if the request is of type POST
    if request.method == "POST":
        # Check if files are added 
        if request.files:
            # Get the image from the request
            image = request.files["image"]
            # Check if the image has a name and extension 
            if image.filename == "":
                print("No filename")
                return redirect(request.url)
            else:
                category  = request.form.get('category')
                if category == '':
                    return False
                date_created  = datetime.strptime(request.form.get('date-created'), '%Y-%M-%d')
                description = request.form.get("description")
                image_name = request.get("image_name")
                if allowed_image(filename=image.filename):
                    filename = secure_filename(image.filename)
                    # create the directory for the files if they don't yet exist
                    image_path = f"/{category}/"
                    image_url = '/static/assets/img'+image_path
                    # now we can save the image 
                    image.save(os.path.join(os.path.join(app.config['UPLOAD_FOLDER']+image_path),filename))
                    print('image uploaded')
                    upload_image = Image(image_name,category,image_url,date_created,description)
                    db.session.add(upload_image)
                    db.session.commit()
    return render_template('admin/upload/upload.html', Title='upload images')

# starting the application
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=80)

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
