from flask import Flask

app = Flask(__name__)

@app.route("/")#127
def index():
    return "<h1>Whats up laude</h1>"

@app.route("/tattu")
def info():
    return "<h1>Tera tatta kaat duga lodu</h1>"

@app.route('/vanshgfs/<name>')
def gf(name):
    if name[-1] == "y":
        return name+"ikful"
    else:
        return name+"y"



if __name__ == '__main__':
    app.run(debug=True)
