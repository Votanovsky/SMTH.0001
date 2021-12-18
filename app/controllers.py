import flask_admin.contrib.sqla as sqla
# from flask_login.utils import login_required
import app.models as models
import app.forms as forms

from flask import flash, redirect, request, render_template, url_for
from flask_login import login_user, current_user
from flask_admin import expose, AdminIndexView
from flask_wtf.form import FlaskForm
from werkzeug.security import generate_password_hash


class ArchiveController:
    def get_exhibitions():
        return models.Exhibition.query.all()

    def get_exhibition_by_id(id = None):
        return models.Exhibition.query.filter_by(id = id).first_or_404()

    def get_exhibition_by_date(year = None, month = None):
        return models.Exhibition.query.filter_by(year = year).filter_by(month = month).first_or_404()


class RouteController:
    form: FlaskForm

    def index(self):
        return render_template("index.html")

    def login(self):
        self.form = forms.AuthForm()
        if request.method.lower() == 'post':
            admin = models.Administrator.query.filter_by(name = self.form.login.data).first()
            if admin:
                if admin.check_password(self.form.password.data):
                    login_user(admin, remember=self.form.remember.data)
                    next = request.args.get('next')
                    if next:
                        return redirect(next)
                    return redirect('/admin')
                else:
                    flash("Incorrect password")
            else:
                flash("Admin not found")
        return render_template("login.html", form = self.form)
    
    def curators(self):
            return render_template("curators.html")


    def err404(self):
        return render_template("status_codes/404.html")


class IndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name):
        return redirect(url_for('login'))


class ModelView(sqla.ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name):
        return redirect(url_for('login'))


class AdminView(ModelView):
    form = forms.AdminForm
    instance = None
    # edit_template = create_template = "/admin/create_edit.html"
    # column_list = dict(ID=models.Administrator.id, Admin_Name=models.Administrator.name)
    column_exclude_list = ('password_hash')

    @expose('/admins/new/', methods=['GET', 'POST'])
    @expose('/admins/edit/', methods=['GET', 'POST'])
    def create_or_edit(self):
        if request.method.lower() == 'post':
            if models.Administrator.query.filter_by(name = request.form.get('login')).first() is not None:
                flash("Admin with such a login already exists", "error")
            elif self.instance:
                self.instance.name = request.form.get('login')
                self.instance.password_hash = generate_password_hash(request.form.get('password'))
                self.session.add(self.instance)
                self.session.commit()
                flash("Admin with id %d edited successfully" % self.instance.id, "info")
                self.instance = None
            else:
                self.instance = models.Administrator(
                    name = request.form.get('login'),
                    password_hash = generate_password_hash(request.form.get('password'))
                )
                self.session.add(self.instance)
                self.session.commit()
                self.instance = None
                flash("Added a new instance to the admins table successfully", "info")
            return redirect('/admins')
        else:
            if request.args.get("id"):
                self.instance = models.Administrator.query.get(int(request.args.get("id")))
        return render_template(self.create_template, form = self.form)
    

class CuratorView(ModelView):
    form = forms.CuratorForm
    instance = None
    # edit_template = create_template = "/admin/create_edit.html"
    # column_list = dict(ID=models.Administrator.id, Admin_Name=models.Administrator.name)
    column_exclude_list = ('password_hash')

    @expose('/curators/new/', methods=['GET', 'POST'])
    @expose('/curators/edit/', methods=['GET', 'POST'])
    def create_or_edit(self):
        if request.method.lower() == 'post':
            #if models.Curator.query.filter_by(name = request.form.get('name')).first() is not None:
            #    flash("Curator with such a name already exists", "error")
            if self.instance:
                self.instance.name = self.form.name.data
                self.instance.description = self.form.description.data
                self.instance.curator_image = self.form.image.data
                self.session.add(self.instance)
                self.session.commit()
                flash("Curator with id %d edited successfully" % self.instance.id, "info")
                self.instance = None
            else:
                self.instance = models.Curator(
                    name = request.form.get('name'),
                    description = request.form.get('description'),
                    curator_image = request.form.get('image')
                )
                self.session.add(self.instance)
                self.session.commit()
                self.instance = None
                flash("Added a new instance to the admins table successfully", "info")
            return redirect('/curators')
        else:
            if request.args.get("id"):
                self.instance = models.Curator.query.get(int(request.args.get("id")))
        return render_template(self.create_template, form = self.form)


class ExhibitionView(ModelView):
    form = forms.ExhibitionForm
    instance = None

    @expose('/exhibitions/new/', methods=['GET', 'POST'])
    @expose('/exhibitions/edit/', methods=['GET', 'POST'])
    def create_or_edit(self):
        if request.method.lower() == 'post':
            if models.Exhibition.query.filter_by(name = request.form.get('name')).first() is not None:
                flash("Exhibition with such a name already exists", "error")
            elif self.instance:
                self.instance.name = request.form.get('name')
                self.instance.month = request.form.get('month')
                self.instance.year = request.form.get('year')
                self.instance.curator_id = self.form.curator.data
                self.session.add(self.instance)
                self.session.commit()
                flash("Exhibition with id %d edited successfully" % self.instance.id, "info")
                self.instance = None
            else:
                self.instance = models.Exhibition(
                    name = request.form.get('name'),
                    month = request.form.get('month'),
                    year = request.form.get('year'),
                    curator_id = request.form.get('curator'),
                )
                self.session.add(self.instance)
                self.session.commit()
                self.instance = None
                flash("Added a new instance to the %s table successfully" % models.Administrator.__tablename__.upper(), "info")
            return redirect('/exhibitions')
        else:
            self.form.curator.choices = ((c.id, c.name) for c in models.Curator.query.all())
            if request.args.get("id"):
                self.instance = models.Exhibition.query.get(int(request.args.get("id")))
        return render_template(self.create_template, form = self.form)