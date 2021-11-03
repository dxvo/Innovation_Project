from flask_wtf import FlaskForm
from wtforms import IntegerField,SubmitField,DecimalField
from wtforms.validators import DataRequired,InputRequired

#Form to get machine data
class Machinedata(FlaskForm):
    machineID = IntegerField('MachineID',validators=[DataRequired()])
    volt = DecimalField('Volt',validators=[DataRequired()])
    rotate = DecimalField('Rotate',validators=[DataRequired()])
    vibration = DecimalField('Vibration',validators=[DataRequired()])
    pressure = DecimalField('Pressure',validators=[DataRequired()])
    model = IntegerField('Model',validators=[DataRequired()])
    age = IntegerField('Age',validators=[DataRequired()])
    comp = IntegerField('Comp',validators=[DataRequired()])
    lastService = IntegerField('Last Service',validators = [InputRequired()])
    lastFailure = IntegerField('Last Failure',validators=[InputRequired()])
    
    submit = SubmitField('Submit')