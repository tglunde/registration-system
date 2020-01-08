from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class contestant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    year_of_birth = db.Column(db.Integer)
    nationality = db.Column(db.String(30))
    telephone = db.Column(db.String(25))
    zip_code = db.Column(db.String(15))
    street = db.Column(db.String(100))
    city = db.Column(db.String(25))
    country = db.Column(db.String(25))
    gender = db.Column(db.String(10))
    club = db.Column(db.String(50))
    contest = db.Column(db.String(20))


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_contestant = contestant(first_name = request.form['firstname'], last_name = request.form['lastname'], 
        email = request.form['email'], street = request.form['street'], telephone = request.form['telephone'],
        year_of_birth = request.form['yob'], nationality = request.form['nationality'], 
        zip_code = request.form['zipcode'], city = request.form['city'], country = request.form['country'],
        gender = request.form['gender'],club = request.form['club'], contest = request.form['contest'])

        db.session.add(new_contestant)
        db.session.commit()

        return redirect(url_for("index"))
    return render_template("signup.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)