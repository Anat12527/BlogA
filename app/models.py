from app import db
from flask_login import  UserMixin
from datetime import date



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
    userPassword = db.Column(db.String(50), nullable=False)
    userActive = db.Column(db.Integer,nullable=False)

    def __init__(self, userId, userName, userPassword,userActive):
        self.userId = userId
        self.userName = userName
        self.userPassword = userPassword
        self.userActive = userActive


class Comment(db.Model):

    __tablename__ = 'comments'
    commentId = db.Column(db.Integer, primary_key=True)
    commentDetail = db.Column(db.String(50), nullable=False)
    commentOwnerId = db.Column(db.Integer,db.ForeignKey('users.userId'))
    commentDate = db.Column(db.DATE, default=date.today(), nullable=False)

    def __init__(self, commentId, commentDetail, commentOwnerId, commentDate):
        self.commentId = commentId
        self.commentDetail = commentDetail
        self.commentOwnerId = commentOwnerId
        self.commentDate = commentDate


class Pictures(db.Model):

    __tablename__ = 'pictures'
    imageId = db.Column(db.Integer, primary_key=True)
#    image = db.Column(db.LargeBinary, nullable=False)
    imageName = db.Column(db.String, nullable=False)

    def __init__(self,imageName):


        self.imageName = imageName














