from flask import Blueprint,render_template,url_for


comment = Blueprint("comment", __name__,template_folder='templates')



@comment.route('/comment',methods = ['GET','POST'])
def page_comment_top():
    print("aaa")
    return render_template('comment/comment_top.html')


@comment.route("/comment_add")
def get_details():
    return "login"


@comment.route("/comment_display")
def receive_details():
    return "done adding"