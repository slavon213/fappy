from flask import render_template
from . import main



@main.route('/')
def func_name():
    return render_template('base.html')
