# Import necessary modules
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bouddha'
csrf = CSRFProtect(app) 

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit   = SubmitField('Login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # ... login logic ...
        return redirect(url_for('home'))
    return render_template('login.html', form=form)  # Pass the form object here