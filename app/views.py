from flask import render_template, redirect, session, url_for, request, g
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/work')
def work():
    return render_template("work.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")
