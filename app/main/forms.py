from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Title Of Pitch', validators=[Required()])
    category = RadioField('Type', choices=[  ('projectpitch','Project pitch'), ('jobpitch','Job pitch'),('businesspitch','Business pitch'),('quotepitch','Quote pitch')],validators=[Required()])
    pitch = TextAreaField('Go ahead and pitch!!', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a Comment', validators=[Required()])
    submit = SubmitField('Submit')

class UpvoteForm(FlaskForm):
    submit = SubmitField('Submit')

class DownvoteForm(FlaskForm):
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us something about you.',validators = [Required()])
    submit = SubmitField('Submit')