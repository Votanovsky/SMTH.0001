# import os
import os
import secrets


class Config:
    FLASK_ADMIN_SWATCH = "yeti"
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test' #os.environ.get("DATABASE_URL") or 'postgresql://localhost/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True
