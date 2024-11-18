from flask import Flask,Blueprint

app = Flask(__name__)

admin_url = Blueprint('admin',__name__,url_prefix="/admin")
app.register_blueprint(admin_url)