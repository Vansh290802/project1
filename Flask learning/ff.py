from flask import Flask, render_template,flash,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = "chut"

class Info(FlaskForm):

    gfname = StringField("Naam daal ludo")
    submit = SubmitField("PRESSSSS MEEEE")

@app.route('/',methods = ["GET","POST"])
def index():

    form = Info()

    if form.validate_on_submit():
        session['gfname'] = form.gfname.data
        flash(f"you just chose: {session['gfname']}".format())

        return redirect(url_for('index'))
    return render_template("ffindex.html",form=form)

if __name__ == '__main__':
    app.run(debug=True)
