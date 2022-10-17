from crypt import methods
from components.pima.services import Pima
from flask import Flask, Blueprint, render_template, url_for, request, redirect, render_template

bp = Blueprint('pima', __name__)

@bp.route('/')
def index() :
    return render_template('pima/index.html', predictions = Pima().get_all())

@bp.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        features = [float(x) for x in request.form.values()]
        
        # validating if features are correctly entered

        predict_new = Pima().predict(features)
        return redirect(url_for('pima.index'))

    return render_template('pima/predict.html')
