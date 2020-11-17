
from flask import Flask,blueprints
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__,static_url_path = '/static', static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:newrootpassword@localhost/book_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey4'
login_manager = LoginManager(app)

login_manager.login_view = 'main.index' #the user returns to this view function.
login_manager.login_message = 'You must login'
#login_manager.anonymous_user = AnonymousUserMixin
db = SQLAlchemy()

db.init_app(app)





from app.users.views import users
from app.posts.views import posts
from app.main.views import main
from app.about.views import about
from app.comment.views import comment



# Register blueprint(s)

app.register_blueprint(users,url_prefix="/users")
app.register_blueprint(posts,url_prefix="/posts")
app.register_blueprint(comment,url_prefix="/comment")
app.register_blueprint(main,url_prefix="/main")
app.register_blueprint(about,url_prefix="/about")



