from flask import Flask, render_template

app = Flask(__name__)  # creating the app


# index route
@app.route("/")
def index():
    return render_template('index.html', Title='Home')


@app.route('/<string:category>')
def get_cat(category):
    print(category)
    return render_template('index.html', Title='category')


@app.route("/EZine")
def e_zine():
    return render_template("ezine.html", Title='ezine')


@app.route('/admin')
def admin():
    return render_template('admin/admin.html', Title="admin")


@app.route('/admin/ezine')
def admin_ezine():
    return render_template('admin/ezine/ezine.html', Title='create zine')


@app.route('/admin/upload')
def admin_upload():
    return render_template('admin/upload/upload.html', Title='upload images')


# starting the application
if __name__ == '__main__':
    app.run(debug=True, port=80)

# We will change this during production and create
# a WSGI server to run it in a docker
# This server is intended to be the api to the EvertRobles website
# to provide it of the necessary data
