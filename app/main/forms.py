from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp
from flask_pagedown.fields import PageDownField
from ..models import Role, User


class EditProfileForm(Form):
    name = StringField('Real name', validators=[Length(min=0, max=64)])
    location = StringField('Location', validators=[Length(min=0, max=64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class EditProfileAdminForm(Form):
    email = StringField('Email', validators=[DataRequired(),
                                             Length(min=1, max=64),
                                             Email()])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=1, max=64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                          'Usernames must have only letters, '
                                                          'numbers, dots or underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(min=0, max=64)])
    location = StringField('Location', validators=[Length(min=0, max=64)])
    about_me = TextAreaField('About Me')
    submit = SubmitField('Submit')

    # used to transform the integer value of a role in a string order by Role.name
    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registred.')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class PostForm(Form):
    body = PageDownField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField("Submit")
