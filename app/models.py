from app import db
from flask_login import UserMixin,AnonymousUserMixin

from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash


class BookPost(db.Model):

    __tablename__ = 'posts'
    postId = db.Column(db.Integer,primary_key = True)
    postTitle = db.Column(db.String(50), nullable=False)
    postBy = db.Column(db.String(50),nullable=False)
    postDate = db.Column(db.DATE, default=date.today(), nullable=False)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.userId'))
    postPictureId = db.Column(db.Integer,db.ForeignKey('pictures.imageId'))
    postDetails = db.Column(db.String(4294000000), nullable=False)
    postExtraDetails = db.Column(db.String(4294000000), nullable=False)
    pic = db.relationship('Pictures',backref='bookp')


#    owner = db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,postId,postTitle,postBy,postDate,ownerId,postPictureId,postDetails,postExtraDetails):
        self.postId = postId
        self.postTitle = postTitle
        self.postBy = postBy
        self.postDate = postDate
        self.ownerId = ownerId
        self.postPictureId = postPictureId
        self.postDetails = postDetails
        self.postExtraDetails = postExtraDetails


class Users(db.Model,UserMixin):

    __tablename__ = 'users'
    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50), nullable=False)
    userPassword_hash = db.Column(db.String(128))
    userActive = db.Column(db.Integer,nullable=False)

    def __init__(self, userId, userName,password,userActive):
        self.userId = userId
        self.userName = userName
        self.userPassword_hash = generate_password_hash(password)
        self.userActive = userActive

    def check_password(self,password):
        return check_password_hash(self.userPassword_hash,password)

    def get_id(self):
        return self.userId

class Anonymous(AnonymousUserMixin):
   def __init__(self):
       self.userName ='Guest'



class Comment(db.Model):

    __tablename__ = 'comments'
    commentId = db.Column(db.Integer, primary_key=True)
    commentDetail = db.Column(db.String(7000), nullable=False)
    commentOwnerId = db.Column(db.Integer,db.ForeignKey('users.userId'))
    commentDate = db.Column(db.DATE, default=date.today(), nullable=False)
    commentPostId = db.Column(db.Integer,db.ForeignKey('posts.postId'))
    postid = db.relationship('BookPost',backref='idpost')
    usercomment = db.relationship('Users',backref='useronpost' )


    def __init__(self, commentId, commentDetail, commentOwnerId, commentDate,commentPostId):
        self.commentId = commentId
        self.commentDetail = commentDetail
        self.commentOwnerId = commentOwnerId
        self.commentDate = commentDate
        self.commentPostId = commentPostId


class Pictures(db.Model):

    __tablename__ = 'pictures'
    imageId = db.Column(db.Integer, primary_key=True)
#    image = db.Column(db.LargeBinary, nullable=False)
    imageName = db.Column(db.String, nullable=False)

    def __init__(self,imageName):


        self.imageName = imageName















