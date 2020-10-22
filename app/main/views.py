from flask import Blueprint,render_template,url_for,flash, get_flashed_messages
from app import db, models
from app.models import BookPost,Pictures
from datetime import datetime




main = Blueprint('main', __name__, url_prefix='/main',static_url_path = '/static', static_folder='static')




@main.route('/',methods = ['GET','POST'])
def index():
#     last_posts = BookPost.query.order_by(BookPost.postId.desc()).limit(2)
     last_posts = db.session.query(BookPost).join(Pictures,Pictures.imageId == BookPost.postPictureId).order_by(BookPost.postId.desc()).limit(2)
     last_posts = last_posts[::-1]
     post_top_page = last_posts[1]
     post_bottom_page = last_posts[0]
     date_post_top = date_to_string_top(post_top_page.postDate)
     date_post_bottom = date_to_string_bottom(post_bottom_page.postDate)
     return render_template('main/index1.html', post_top_page=post_top_page, post_bottom_page=post_bottom_page,date_post_top = date_post_top,date_post_bottom = date_post_bottom)



@main.route('/date_to_string_top/<date_post_top>',methods =['GET','POST'])
def date_to_string_top(date_post_top):
    dateStr_top = date_post_top.strftime("%d-%b-%Y ")
    return dateStr_top

@main.route('/date_to_string_bottom/<date_post_bottom>',methods =['GET','POST'])
def date_to_string_bottom(date_post_bottom):
    dateStr_bottom =  date_post_bottom.strftime("%d-%b-%Y ")
    return  dateStr_bottom


#@main.route('/')













