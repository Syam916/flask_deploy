# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
import mysql.connector
from flask import current_app

main = Blueprint('main', __name__)

def get_db_connection():
    return mysql.connector.connect(
        host=current_app.config['DB_HOST'],
        user=current_app.config['DB_USER'],
        password=current_app.config['DB_PASSWORD'],
        database=current_app.config['DB_NAME']
    )

@main.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to the database and retrieve the user
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users_fake_data WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        db.close()

        # Verify the password
        if user and check_password_hash(user['password'], password):
            session['username'] = user['username']
            return redirect(url_for('main.welcome'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@main.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('main.login'))
    return f"Welcome, {session['username']}!"
