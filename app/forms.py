from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import BooleanField, FileField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AuthForm(FlaskForm):
    login = StringField("Login:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")


class AdminForm(FlaskForm):
    login = StringField("Login:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    submit = SubmitField("Save")


class CuratorForm(FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    description = TextAreaField("Description:", validators=[DataRequired()])
    image = FileField("Image:", validators=[DataRequired()])


class ExhibitionForm(FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    month = SelectField("Month:", coerce=int, choices=[(1, "January"),(2, "February"),(3, "March"),(4, "April"),
        (5, "May"),(6, "Jume"),(7, "July"),(8, "August"),
        (9, "September"),(10, "October"),(11, "November"),(12, "December")
    ], validators=[DataRequired()])
    year = SelectField("Year:", coerce=int, choices=((year, year) for year in range(2019, 2091)), validators=[DataRequired()])
    curator = SelectField("Curator:", coerce=int, validators=[DataRequired()])