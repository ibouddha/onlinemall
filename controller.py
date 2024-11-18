from flask import session
from models import user_models as um


def user_authenticate(email,password):
    user = um.getLoggedUser(email,password)
    # print(user)
    if user:
        return user
    else:
        return None

def is_user_connected(username):
    checked = vm.checkConnection(username)
    print(checked)
    return checked

def authentified(username):
    if username in session:
        um.update_status(username)
        return (f'{username} is now authenticated')
    else:
        return (f'{username} is not authenticated')