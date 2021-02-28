from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
import email_validator
from wtforms.validators import Required

class PitchForm(FlaskForm):
    my_category = SelectField('Category', choices=[('Product','Product'),('Marketing','Marketing'),('Punch Lines','Punch Lines'),('Pickup Lines', 'Pickup Lines')],validators=[Required()])
    my_pitches = TextAreaField('Enter Your Pitch', validators=[Required()])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Leave Your Comments Below..', validators=[Required()])
    submit = SubmitField('Submit Comments')
    
class BioForm(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')