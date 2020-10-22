from flask import Blueprint,render_template,url_for,request,redirect, flash, get_flashed_messages
from app import db
from app.models import Users
from flask_login import LoginManager
from app import login_manager

users = Blueprint('users', __name__,template_folder='templates')

@login_manager.user_loader
def get_user_id(userId):
    """Returns an the user id as integer.receives id_user  ."""
    return Users.query.get(int(userId))

@users.route("/userlogin",methods=['POST','GET'])
def user_valid_reg():

    if request.method == 'POST':

       user_name_entered = request.form.get('user_name')
       password_name_entered = request.form.get('password')
       if user_name_entered.isalpha() or user_name_entered.isnumeric():
          print("enter")
          flash("jj hkhkj")
          return redirect(url_for('main.index'))
       else:
           add_user(user_name_entered,password_name_entered)
    else:
           return redirect(url_for('main.index'))





@users.route("/add_user/<user_name_entered>/<password_name_entered>")
def add_user(user_name_entered,password_name_entered):
    users_details = Users(None, user_name_entered, password_name_entered, '1')
    db.session.add(users_details)
    db.session.commit()
    "print regestation success"
    return redirect(url_for('main.index'))


@users.route("/add_post")
def addpost():
    print("uuu")
    return render_template('users/users.html')
