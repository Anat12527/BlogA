from flask import Blueprint,render_template,url_for
from flask_login import current_user



about = Blueprint("about", __name__,template_folder='templates')


@about.route('/about', methods=['POST', 'GET'])
def about_me():
    if current_user.is_anonymous:
        return render_template('about/about.html',user='Guest')
    else:
        return render_template('about/about.html', user=current_user.userName)

@about.route('/reading',methods=['POST','GET'])
def reading():
    if current_user.is_anonymous:
        return render_template('about/reading.html', user='Guest')
    else:
        return render_template('about/reading.html',user=current_user.userName)

@about.route('/favorites',methods =['POST','GET'])
def favorites():
    if current_user.is_anonymous:
       return render_template('about/favorites.html',user='Guest')
    else:
       return render_template('about/favorites.html', user=current_user.userName)








