from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Contestant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(10))
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    year_of_birth = db.Column(db.Integer)
    telephone = db.Column(db.String(25))
    club = db.Column(db.String(50))
    contest = db.Column(db.String(25))
    confirmation = db.Column(db.String())
    time = db.Column(db.DateTime(), default=datetime.datetime.now())
    active = db.Column(db.Boolean(), default=False)
    ip = db.Column(db.String(16))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():


    if request.method == 'POST':
        new_contestant = Contestant(first_name = request.form['firstname'], last_name = request.form['lastname'], 
        email = request.form['email'], telephone = request.form['telephone'],
        year_of_birth = request.form['yob'], contest = request.form['contest'],
        gender = request.form['gender'],club = request.form['club'], ip = request.environ['REMOTE_ADDR'])

        db.session.add(new_contestant)
        db.session.commit()

        return redirect(url_for("index"))
    return render_template("signup.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)