from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    mylist = [12,34,56,7,7,8,99]
    name = "vansh"
    letters = list(name)
    vanshgf = {'college':100}
    gfs = ["tosh","bashi","thorny","tickly"]
    return render_template("basic.html",name = name,letters=letters,vanshgf=vanshgf,mylist = mylist,gfs=gfs)

if __name__ == '__main__':
    app.run(debug=True)
