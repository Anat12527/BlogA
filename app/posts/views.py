from flask import Blueprint,render_template,url_for
from app import db
from app.models import BookPost,Pictures
from flask import request,redirect
from collections import defaultdict,Counter
import calendar
from sqlalchemy import extract
from flask_login import login_required,current_user,login_manager


posts = Blueprint('posts', __name__,template_folder='templates')


@posts.route('/posts_show',methods = ['POST','GET'])
@login_required
def posts_show ():

    return render_template('posts/post_show.html', user=current_user.userName)

@posts.route('/post_get_details',methods =['POST','GET'])
@login_required
def post_get_details():
    post_title_entered = request.form.get('post_title')
    post_author_entered = request.form.get('post_author')
    post_date_entered = request.form.get('post_date')
    post_owner_id_entered = request.form.get('post_owner_id')
    picture_path_entered = request.form.get('image_name')
    post_details_entered = request.form.get('post_details')
    post_extra_entered = request.form.get('post_extra_details')
    print(picture_path_entered)

    return post_title_entered,post_author_entered, post_date_entered, post_owner_id_entered, picture_path_entered ,post_details_entered,post_extra_entered

@posts.route('/add_post',methods=['POST','GET'])
@login_required
def post_add():
    if request.method == 'POST':
       post_title_entered ,post_author_entered, post_date_entered, post_owner_id_entered,picture_path_entered,post_details_entered,post_extra_entered,= post_get_details()
       image_detail_entered = Pictures(picture_path_entered)
       db.session.add(image_detail_entered)
       db.session.commit()
       pic_datails = db.session.query(Pictures).filter(Pictures.imageName == picture_path_entered).first()
       post_details_entered = BookPost(None,post_title_entered,post_author_entered, post_date_entered, post_owner_id_entered, pic_datails.imageId,post_details_entered,post_extra_entered)
       db.session.add(post_details_entered)
       db.session.commit()
       return redirect(url_for('main.index'))


@posts.app_template_filter('month_number')
@login_required
def month_name(month_number):
    return calendar.month_name[month_number]


@posts.route('/posts_archive',methods=['POST','GET'])
@login_required
def display_posts():
    all_posts = BookPost.query.all()
    post_dict_list = defaultdict(list)
    for post in all_posts:
        post_dict_list[post.postDate.year].append(post.postDate.month)
    dict_a = {}
    for k_year,val_month in post_dict_list.items():
        dict_a[k_year] = Counter(val_month)
    dict_b = {}
    # add the monthly and yearly totals counts
    posttotal = 0
    for key, value in dict_a.items():
        yearsum = 0
        for month, c in value.items():
            yearsum += c
            posttotal += c
            dict_b[key] = yearsum

    post_total_dict = defaultdict(list)
    for d in (dict_a,dict_b):
        for key,value in d.items():
           post_total_dict[key].append(value)
    print(post_total_dict)
    if  current_user.is_anonymous:
         return render_template('posts/all_posts.html',d=post_total_dict,all_posts=all_posts,user='Guest')
    else:
        return render_template('posts/all_posts.html', d=post_total_dict, all_posts=all_posts,user=current_user.userName)


@posts.route('/post_by_month/<int:year>/<int:month>',methods=['POST','GET'])
@login_required
def post_by_month(year,month):
    if request.method == 'GET':
       posts_m = db.session.query(BookPost).filter(extract('year',BookPost.postDate)==year).all()
       print(posts_m)
       return redirect(url_for('posts.posts_show'))



@posts.route('/post_to_delete/<int:post_id>',methods=['POST','GET'])
@login_required
def post_to_delete(post_id):
    if request.method == 'GET':
       all_posts = BookPost.query.all()
       return render_template('posts/post_show.html', user=current_user.userName,all_posts = all_posts)
    return render_template('posts/post_show.html', user=current_user.userName)


@posts.route('/show_table_posts',methods=['POST','GET'])
@login_required
def show_table_posts():
    all_posts = BookPost.query.all()
    return render_template('posts/post_show.html', user=current_user.userName, all_posts=all_posts)




