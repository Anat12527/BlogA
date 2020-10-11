
from flask import Flask,blueprints
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate


app = Flask(__name__,static_url_path = '/static', static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:newrootpassword@localhost/book_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey4'
db = SQLAlchemy()
#Migrate = (app,db)
db.init_app(app)

# Register blueprint(s)


#
from app.users.views import users
from app.posts.views import posts
from app.main.views import main
from app.about.views import about
from app.comment.views import comment

app.register_blueprint(users,url_prefix="/users")
app.register_blueprint(posts,url_prefix="/posts")
app.register_blueprint(comment,url_prefix="/comment")
app.register_blueprint(main,url_prefix="/main")
app.register_blueprint(about,url_prefix="/about")
#app.register_blueprint(main, subdomain='main')



