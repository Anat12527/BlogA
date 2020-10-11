from flask import Blueprint,render_template,url_for




about = Blueprint("about", __name__,template_folder='templates')


@about.route('/about', methods=['POST', 'GET'])
def about_me():
    print("bbb")
    return render_template('about/about.html')

@about.route('/reading',methods=['POST','GET'])
def reading():
    return render_template('about/reading.html')

@about.route('/favorites',methods =['POST','GET'])
def favoriets():
    return render_template('about/favorites.html')








