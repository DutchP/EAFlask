from flask import Flask, render_template

app = Flask(__name__)  # creating the app

# index route
@app.route("/")
def index():
    return render_template('index.html', Title='Home')

# starting the application
if __name__ == '__main__':
    app.run(debug=True, port=80)

# We will change this during production and create
# a WGSI server to run it in a docker
# This server is intended to be the api to the EvertRobles website 
# to provide it of the necessary data 