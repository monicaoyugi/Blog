from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class BlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    post = TextAreaField('Blog', validators=[DataRequired()])
    submit = SubmitField('Submit')


class CommentsForm(FlaskForm):
    comment = TextAreaField('Comments', validators=[DataRequired()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.', validators=[DataRequired()])
    submit = SubmitField('Submit')
