from flask import Flask, Blueprint, request, session, render_template
import controller as ctrl
from models import user_models as um
from models import vendeur_models as vm
from models import store_models as store

app = Flask(__name__)

user_route = Blueprint('user',__name__,url_prefix='/user')

@user_route.route('/')
def home():
    if('username' in session):
        if (um.get_user_role(session['username']) == 'admin'):
            return render_template('admin/home.html')
        elif (um.get_user_role(session['username']) == 'vendeur'):
            return render_template('vendeur/home.html')
    else:
        return render_template('users/home.html')


@user_route.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = ctrl.user_authenticate(email, password)
        # print(user)
        if user:
            username = user[2]
            ctrl.authentified(username)
            # print(username)
            session['username'] = username
            if (um.get_user_role(session['username']) == 'admin'):
                return render_template('admin/home.html', role="admin")
            elif (um.get_user_role(session['username']) == 'vendeur'):
                return render_template('vendeur/home.html', role="vendeur")
            else:
                return render_template('users/home.html')
        else:
            return render_template('users/home.html')
            
            
@user_route.route('/register')
def register():
    
    if request.method == 'POST':
        name    = request.form['name']
        surname = request.form['surname']
        email   = request.form['email']
        password = request.form['password']
        role    = request.form['role']
        status  = 'offline'
        store_id = store.getIdByName(request.form['store'])
        user = um.users(name,surname,username,email,password,role,status,store_id)
        
    
    return render_template('users/register.html')