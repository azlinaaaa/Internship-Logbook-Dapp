from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from stellar_utils import hash_log, store_hash_on_stellar
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/internship.db'
db = SQLAlchemy(app)
print("SECRET KEY:", os.getenv("SECRET_KEY"))
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))


class Logbook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.String(100))
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    log_hash = db.Column(db.String(200))
    stellar_tx = db.Column(db.String(300))


@login_manager.user_loader

def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        flash('Registration successful')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))

        flash('Invalid credentials')

    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    logs = Logbook.query.filter_by(student=current_user.username).all()
    return render_template('dashboard.html', logs=logs)

@app.route('/submit', methods=['GET', 'POST'])
@login_required
def submit_log():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        combined = title + content + current_user.username

        generated_hash = hash_log(combined)

        stellar_response = store_hash_on_stellar(generated_hash)

        transaction_hash = stellar_response['hash']

        new_log = Logbook(
            student=current_user.username,
            title=title,
            content=content,
            log_hash=generated_hash,
            stellar_tx=transaction_hash
        )

        db.session.add(new_log)
        db.session.commit()

        flash('Logbook submitted successfully')

        return redirect(url_for('dashboard'))

    return render_template('submit_log.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()
    app.run(debug=True)
else:
    
    with app.app_context():
        db.create_all()

    app.run(debug=True)
