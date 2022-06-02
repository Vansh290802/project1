from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("formindex.html")

@app.route('/signup_form')
def signup_form():
    return render_template("formsignup.html")

@app.route('/thank_u')
def thank_u():
    contains_digit_first = False
    contains_digit_last = False
    first = request.args.get('first')
    last = request.args.get('last')

    contains_digit_first = any(map(str.isdigit, first))
    contains_digit_last = any(map(str.isdigit, last))

    final = contains_digit_first and contains_digit_last

    return render_template("formthanku.html",first=first,last=last,contains_digit_first=contains_digit_first,contains_digit_last=contains_digit_last)

@app.errorhandler(404)
def page_not_found(canbeanything):
    return render_template("404.html"), 404









if __name__ == '__main__':
    app.run(debug=True)
