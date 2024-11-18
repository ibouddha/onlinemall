from flask import Flask, Blueprint, render_template, url_for, session
import models.vendeur_models as vm
import controller as ctrl

app = Flask(__name__)

# Define the blueprint with a URL prefix
vendeur_url = Blueprint('vendeur', __name__, url_prefix='/vendeur')


@vendeur_url.route('/')
def index():
    return 'vendeur home'
   
            
@vendeur_url.route('/profile')
def profile():
    return 'User profile'

