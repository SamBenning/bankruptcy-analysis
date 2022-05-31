from flask import Blueprint
import base64
from io import BytesIO

from matplotlib.figure import Figure

views = Blueprint('views', __name__)

@views.route('/')
def home():
    # Generate the figure **without using pyplot**
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1,2])
    # Save it to a temporary buffer
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

@views.route('/enter-info')
def enter_info():
    return "Here you will enter your information"