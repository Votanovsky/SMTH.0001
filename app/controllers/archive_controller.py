# from app import db
# import app.models as models


def get_exhibitions():
    return 1 # models.Exhibition.query.all()


def get_exhibition_by_id(id = None):
    return 1 # models.Exhibition.query\
    #    .filter_by(id = id).first_or_404() \
    # if id and id == "<class \'int\'>" else "404"

def get_exhibition_by_date(year = None, month = None):
    return 1 # models.Exhibition.query\
    #    .filter_by(year = year)\
    #    .filter_by(month = month).first_or_404() \
    # if year and month else "404"
