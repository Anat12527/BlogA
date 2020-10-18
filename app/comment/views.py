from flask import Blueprint,render_template,url_for
from app import db, models
from app.models import BookPost
from app.main.views import date_to_string_top

comment = Blueprint("comment", __name__,template_folder='templates')



@comment.route('/comment/<int:post_id>/<string:name>',methods = ['GET','POST'])
def page_comment_top(post_id,name):
    print(post_id)

    post_top_page = db.session.query(BookPost).filter(BookPost.postId == post_id).first()
    date_post_top = date_to_string_top(post_top_page.postDate)
    return render_template('comment/comment_top.html',post_top_page=post_top_page,name=name,date_post_top=date_post_top)


@comment.route("/comment_add")
def get_details():
    return "login"


@comment.route("/comment_display")
def receive_details():
    return "done adding"