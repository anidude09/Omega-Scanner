from flask_wtf import FlaskForm
from wtforms import SelectField
from core.etc.ParseJson import RenderJson

command = RenderJson()
choices = command['title']

class Form(FlaskForm):
    dorksList = SelectField('Dorks', choices=choices)
