from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('template.html')

@app.route("/hi/")
def who():
    return "Who are you?"

@app.route("/hi/<username>")
def greet(username):
    return f"Hi there, {username}!"

t = Template("Hello {{ something }}")

@app.route("/hi/template")
def myTemplate():
    return t.render(something="World")