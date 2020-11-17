from flask import Blueprint,render_template,redirect,url_for,request
from app import db, models
from app.models import BookPost,Comment
from app.main.views import date_to_string_top
from flask_login import login_required,current_user
from datetime import date


comment = Blueprint("comment", __name__,template_folder='templates')



@comment.route('/comment/<int:post_id>/<string:name>',methods = ['GET','POST'])
@login_required
def page_comment_top(post_id,name):
    print(post_id)
    page = request.args.get('page', 1, type=int)
    pagination = db.session.query(Comment).filter(Comment.commentPostId==post_id).order_by(Comment.commentDate.desc()).paginate(
        page, per_page=3, error_out=False)
    comments = pagination
    post_top_page = db.session.query(BookPost).filter(BookPost.postId == post_id).first()
    date_post_top = date_to_string_top(post_top_page.postDate)
    return render_template('comment/comment_top.html',post_top_page=post_top_page,name=name,date_post_top=date_post_top,comments=comments,user=current_user.userName)


@comment.route("/add_comment/<int:post_comment_id>",methods = ['GET','POST'])
@login_required
def add_comment(post_comment_id):
    if request.method == 'POST':
       comment_entered = request.form.get("comment_details")
       user_id_logged =  current_user.userId
       today_date = date.today()
       user_comment = Comment (None,comment_entered,user_id_logged,today_date,post_comment_id)
       db.session.add(user_comment)
       db.session.commit()
       post_top_page = db.session.query(BookPost).filter(BookPost.postId == post_comment_id).first()
       name = post_top_page.pic.imageName
       return redirect(url_for('comment.page_comment_top',post_id=post_comment_id,name=name))


@comment.route("/comment_choose")
def comment_choose():
    return "done adding"
