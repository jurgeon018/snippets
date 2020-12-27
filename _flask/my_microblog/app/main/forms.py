from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length, Email
from app.models import User
from flask_login import current_user

class PostForm(FlaskForm):
    body = StringField('Write Your Post', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Send Message')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    image_file = FileField('Upload Pictue', validators=[DataRequired(), FileAllowed(['jpg','jpeg','png'])])
    about_me = TextAreaField('About Me')
    submit = SubmitField('Update')
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=self.username.data).first()
            if user:
                raise ValidationError('Please use a different username.')

class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=0, max=140)])
    submit = SubmitField('Submit')
