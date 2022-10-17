from flask import Flask, Blueprint, render_template

bp = Blueprint('pima', __name__)

@bp.route('/')
def index() :
    return render_template('pima/index.html')