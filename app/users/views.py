from flask import Blueprint,render_template,url_for
#from blueprints import db
#from blueprints.models import Users



users = Blueprint('users', __name__,template_folder='templates')


@users.route("/userlogin")
def userlogin():
    return "login"


@users.route("/add_post")
def addpost():
    print("uuu")
    return render_template('users/users.html')
