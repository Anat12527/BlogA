from flask import Blueprint,render_template,url_for
from app import db
from app.models import BookPost,Pictures
from flask import request,redirect
from sqlalchemy import desc


posts = Blueprint('posts', __name__,template_folder='templates')


@posts.route('/posts_show',methods = ['POST','GET'])
def posts_show ():
 #   pictures = Pictures.query.all()
    return render_template('posts/post_show.html')


@posts.route('/post_get_details',methods =['POST','GET'])
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
def post_add():
    if request.method == 'POST':
       post_title_entered ,post_author_entered, post_date_entered, post_owner_id_entered,picture_path_entered,post_details_entered,post_extra_entered,= post_get_details()
       image_detail_entered = Pictures(picture_path_entered)
       db.session.add(image_detail_entered)
       db.session.commit()
       pic_datails = db.session.query(Pictures).filter(Pictures.imageName == picture_path_entered).first()
       print(pic_datails.imageId)

       post_details_entered = BookPost(None,post_title_entered,post_author_entered, post_date_entered, post_owner_id_entered, pic_datails.imageId,post_details_entered,post_extra_entered)
       print(BookPost)
       db.session.add(post_details_entered)
       db.session.commit()
       return redirect(url_for('main.index'))



#@posts.route('/post_update',methods=['POST','GET'])
#def post_update():
#    last_posts = BookPost.query.order_by(BookPost.postId .desc()).limit(2)
 #   last_posts = last_posts[::-1]
#    print(last_posts[0].postTitle)
   # post_top_page = last_posts[0]
   # post_bottom_page = last_posts[1]
 #  return render_template('main/index1.html')




#@posts.route('/add_picture/<path:picture_location>',methods=['POST','GET'])
#def add_picture(picture_location):
 #   with open(picture_location,'rb') as file:
#        binary_data = file.read()
 #   print(binary_data)
 #   new_picture =  Pictures(binary_data)
  #  db.session.add(new_picture)
  #  db.session.commit()
  #  return redirect(url_for('posts.posts_show'))


#@posts.route('/show_book_pic',methods =['POST','GET'])
#def post_picture():
   # pictures = Pictures.query.all()
    #for picture in pictures:
        #print(picture.imageId,picture.image)
    #return redirect(url_for('posts.posts_show',pictures = pictures))

