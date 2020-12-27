from wtforms import Form, StringField, TextAreaField
from flask_wtf import FlaskForm

class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
