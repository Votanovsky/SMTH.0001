from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login


class Administrator(UserMixin, db.Model):
    __tablename__ = "admins"
    id = db.Column( "id", db.Integer, primary_key = True )
    name = db.Column( "name", db.String(32), unique = True, nullable = False )
    password_hash = db.Column( "password_hash", db.String, nullable = False )

    def set_password(self, raw):
        self.password_hash = generate_password_hash(raw)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Curator(db.Model):
    __tablename__ = "curators"
    id = db.Column( "id", db.Integer, primary_key = True )
    name = db.Column( "name", db.String, nullable = False )
    description = db.Column( "description", db.String, nullable = False )
    curator_image = db.Column( "curator_image", db.String, nullable = False )


class Exhibition(db.Model):
    __tablename__ = "exhibitions"
    id = db.Column( "id", db.Integer, primary_key = True )
    name = db.Column( "name", db.String, nullable = False )
    curator_id = db.Column( "curator_id", db.Integer, db.ForeignKey("curators.id"), nullable = False )
    month = db.Column( "month", db.Integer, nullable = False )
    year = db.Column( "year", db.Integer, nullable = False )


class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column( "id", db.Integer, primary_key = True )
    name = db.Column( "name", db.String, nullable = False )
    author_image = db.Column( "authors_image", db.String, nullable = False )
    pictures = db.relationship( "Picture", secondary="ap_connection", backref=db.backref('authors') )


class Picture(db.Model):
    __tablename__ = "pictures"
    id = db.Column( "id", db.Integer, primary_key = True )
    name = db.Column( "name", db.String, nullable = False )
    exhibition_id = db.Column( "exhibition_id", db.Integer, db.ForeignKey("exhibitions.id"), nullable = False )


class AP_CONNECTION(db.Model):
    __tablename__ = "ap_connection"
    id = db.Column( "id", db.Integer, primary_key = True )
    author_id = db.Column( "author_id", db.Integer, db.ForeignKey("authors.id"), nullable = False )
    pictures_id = db.Column( "picture_id", db.Integer, db.ForeignKey("pictures.id"), nullable = False )


@login.user_loader
def load_user(id):
    return Administrator.query.get(int(id))
