from flask import Flask, render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,BooleanField,
                        DateTimeField,RadioField,
                        SelectField,TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = "laude"

class Info(FlaskForm):

    gfname = StringField("Name of the gf please?",validators=[DataRequired()])
    virgin = BooleanField("Are you virgin")
    gay = RadioField("Are you gay?",choices=[('yep','yes'),('very','very much gay')])
    girl = SelectField("Please pick your gurl",choices=[('t','tosh'),('r','rhea'),('j','jheta')])
    feedback = TextAreaField()
    submit = SubmitField("Submit")

@app.route('/',methods = ["GET","POST"])
def index():

    form = Info()

    if form.validate_on_submit():
        session["gfname"] = form.gfname.data
        session["virgin"] = form.virgin.data
        session["gay"] = form.gay.data
        session["girl"] = form.girl.data
        session["feedback"] = form.feedback.data

        return redirect(url_for('thankyou'))
    return render_template('ff1.html',form=form)

@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")

if __name__ == '__main__':
    app.run(debug=True)
