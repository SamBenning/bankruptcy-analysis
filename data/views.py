from flask import Blueprint, render_template, request, redirect, url_for
import base64
from io import BytesIO
import pandas as pd
import numpy as np
from . import model

from matplotlib.figure import Figure

views = Blueprint('views', __name__)

@views.route('/')
def home():
    # # Generate the figure **without using pyplot**
    # fig = Figure()
    # ax = fig.subplots()
    # ax.plot([1,2])
    # # Save it to a temporary buffer
    # buf = BytesIO()
    # fig.savefig(buf, format="png")
    # # Embed the result in the html output
    # data = base64.b64encode(buf.getbuffer()).decode("ascii")
    # return f"<img src='data:image/png;base64,{data}'/>"
    return render_template("home.html")

@views.route('/enter-info', methods=["GET", "POST"])
def enter_info():

    if request.method == "POST":

        input_values = []
        form = request.form

        for item_key in form:
            item_value = form.get(item_key)
            if item_value:
                input_values.append(float(item_value))
            else:
                input_values.append(None)

        print("INPUT VALUE SIZE: " + str(len(input_values)))

        # return(str(len(input_values)))
        return redirect(url_for('views.results', input_values=input_values))

    return render_template('predict.html')

@views.route('/results/<input_values>')
def results(input_values):


    input_values = input_values[1:len(input_values)-1]
    input_values = input_values.split(',')
    input_values.insert(0, '1')
    for k, value in enumerate(input_values):
        value = value.strip()
        if value == 'None':
            value = -1
        else:
            value = float(value)
        input_values[k] = value

    print(len(input_values))
    ndarray = np.array(input_values)
    print(ndarray.shape)

    my_model = model.Model(ndarray)
    result = my_model.predict()

    return render_template("results.html", input_values=input_values, result=result)