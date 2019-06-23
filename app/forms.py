from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp

class InputForm(FlaskForm):
    input_word= StringField(label='Enter a word', validators=[
        DataRequired(),
        Regexp('^[a-zA-Z\' ]*$', message='Field must contain only letters')
    ])
    submit = SubmitField('Check it!')
