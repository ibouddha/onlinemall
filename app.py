# Import necessary modules
from flask import Flask, render_template, request, session, redirect
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from flask_wtf.csrf import CSRFProtect
from blueprints.vendeur.vendeur import vendeur_url
from blueprints.admin.admin import admin_url
from blueprints.users.users import user_route


app = Flask(__name__)

app.config['SECRET_KEY'] = 'bouddha'
app.register_blueprint(vendeur_url)
app.register_blueprint(admin_url)
app.register_blueprint(user_route)
# csrf = CSRFProtect(app) 

@app.route("/")
def home():
    return render_template('users/home.html')  # Render the home page template  # Add any necessary logic for home page here  # Redirect to the desired page after successful login  # Example: return redirect(url_for('admin.home'))  # Replace 'admin.home' with the desired blueprint and function name  # For example, if the admin blueprint has a function named 'home'

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from the session
    return redirect('/')  # Render the home page template after logout  # Add any necessary logic for logout page here
    
    
if __name__ == "__main__":
    app.run(debug=True) 