from flask import Blueprint, render_template
# from forms import UserLoginForm, UserRegisterForm

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signin')
def signin():
    # form = UserLoginForm()
    return render_template('signin.html')
    # form=form add this after ^

@auth.route('/signup')
def signup():
    # form = UserRegisterForm()
    return render_template('signup.html')
    # form=form add this after ^

@auth.route('/signout')
def signout():
    return render_template('signout.html')