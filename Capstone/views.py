from flask import Flask, Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
import base64
from io import BytesIO
import pandas as pd
import numpy as np
from Capstone import model


views = Blueprint('views', __name__)

app = Flask(__name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)



@views.route('/enter-info', methods=["GET", "POST"])
@login_required
def enter_info():

    if request.method == "POST":
        input_values = []
        form = request.form
        print(form)
        for item_key in form:
            item_value = form.get(item_key)
            if item_value:
                input_values.append(float(item_value))
            else:
                input_values.append(None)

        print("INPUT VALUE SIZE: " + str(len(input_values)))

        # return(str(len(input_values)))
        return redirect(url_for('views.results', input_values=input_values))

    return render_template('predict.html', user=current_user)

@views.route('/results/<input_values>')
@login_required
def results(input_values):

    print(input_values)
    input_values = input_values[1:len(input_values)-1]
    input_values = input_values.split(',')
    for k, value in enumerate(input_values):
        value = value.strip()
        if value == 'None' or value == '':
            value = -1
        else:
            value = float(value)
        input_values[k] = value

    print(len(input_values))
    ndarray = np.array(input_values)
    print(ndarray.shape)

    my_model = model.Model(ndarray)
    result = my_model.predict()[0]

    return render_template("results.html", input_values=input_values, result=result, user=current_user)