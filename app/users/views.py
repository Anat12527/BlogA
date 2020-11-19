from flask import Blueprint,render_template,url_for,request,redirect,flash
from app import db
from app.models import Users
from flask_login import login_user,logout_user
from app import login_manager

users = Blueprint('users', __name__,template_folder='templates')

@login_manager.user_loader
def get_user_id(userId):
    """Returns an the user id as integer.receives id_user  ."""
    return Users.query.get(int(userId))



@users.route("/user_registration/<user_name_entered><password_name_entered>",methods=['POST','GET'])
def user_registration(user_name_entered,password_name_entered):
       print(user_name_entered,password_name_entered)
       if user_name_entered.isalpha() or user_name_entered.isnumeric():
          return redirect(url_for('main.index'))
       else:
           try:
             assert query_user(user_name_entered)
           except AssertionError:
             add_user(user_name_entered, password_name_entered)
             flash(f'Welcome {user_name_entered} !! now please log in')
             return redirect(url_for('main.index'))
           else:
             flash("the user name exist!")
             return redirect(url_for('main.index'))



@users.route("log_in",methods=['POST','GET'])
def log_in():
    if request.method == 'POST':
       user_name_entered = request.form.get('user_name')
       password_name_entered = request.form.get('password')
       if request.form.get('send') =='sign in':
          user = query_user(user_name_entered)
          if user and user.check_password(password_name_entered):
             login_user(user, remember=True)
             return redirect(url_for('main.index'))
          else:
              flash("Either your user name is incorrect or password is incorrect.")
       else:# if user choose to register
           user_registration(user_name_entered,password_name_entered)

       return redirect(url_for('main.index'))

@users.route("log_out",methods=['POST','GET'])
def log_out():
    logout_user()
    return redirect(url_for('main.index'))


@users.route("/add_user/<user_name_entered>/<password_name_entered>")
def add_user(user_name_entered,password_name_entered):
    users_details = Users(None, user_name_entered, password_name_entered, '1')
    db.session.add(users_details)
    db.session.commit()
    "print regestation success"
    return redirect(url_for('main.index'))


@users.route("/query_user/user_name")
def query_user(user_name):
    user_details = db.session.query(Users).filter(Users.userName == user_name).first()
    return user_details


