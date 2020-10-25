from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Title Of Pitch', validators=[Required()])
    category = RadioField('Which Category would you like to Pitch?', choices=[('projectpitch', 'projectpitch'), ('jobpitch', 'jobpitch'), ('businesspitch', 'businesspitch', 'businesspitch'), ('quotepitch', 'quotepitch'), validators=[Required()]])
    pitch = TextAreaField('Go ahead and pitch!!', validators=[Required()])

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a Comment', validators=[Required()])
    submit = SubmitField('Submit')

class UpvoteForm(FlaskForm):
    submit = SubmitField('Submit')

class DownvoteForm(FlaskForm):
    submit = SubmitField('Submit')