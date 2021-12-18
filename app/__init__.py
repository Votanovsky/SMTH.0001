from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_admin import Admin
# from flask_mail import Mail

app = Flask(__name__)
# db = SQLAlchemy(app)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
# from flask_mail import Mail
from config import Config


app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app.controllers import IndexView, ModelView, AdminView, ExhibitionView, CuratorView
from flask_admin import Admin
from app.models import Administrator, Exhibition, Curator, Author, Picture

admin = Admin(app, name="SMTH0001", index_view=IndexView(), template_mode="bootstrap4")
admin.add_view(AdminView(Administrator, db.session, name="Admins", endpoint="admins"))
admin.add_view(ExhibitionView(Exhibition, db.session, name="Exhibitions", endpoint="exhibitions"))
admin.add_view(CuratorView(Curator, db.session, name="Curators", endpoint="curators"))
admin.add_view(ModelView(Author, db.session, name="Authors", endpoint="authors"))
admin.add_view(ModelView(Picture, db.session, name="Pictures", endpoint="pictures"))

from app import routes
