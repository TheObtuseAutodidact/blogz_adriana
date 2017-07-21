from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, StringField, TextAreaField,DateField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.widgets import HiddenInput

class LoginForm(FlaskForm):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username = TextField(
        'username',
        validators=[DataRequired(), Length(min=3, max=20)]
    )
    email = TextField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=20)]
    )
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=3, max=20)]
    )
    confirm = PasswordField(
        'Confirm password',
        validators=[
            DataRequired(), EqualTo('password', message='Passwords must match.')
        ]
    )


class NewPostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    body = TextAreaField('body', validators=[DataRequired()])
    pub_date = DateField('pub_date', format='%Y-%m-%d')
    author_id = IntegerField('author_id', widget=HiddenInput())
