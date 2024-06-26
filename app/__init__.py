import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.info import context

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', **context, url=os.getenv("URL"))

@app.route('/about')
def about():
    return render_template('about.html', **context, url=os.getenv("URL"))

@app.route('/work')
def work():
    return render_template('work.html', **context, url=os.getenv("URL"))

@app.route('/hobby')
def hobby():
    return render_template('hobby.html', **context, url=os.getenv("URL"))

@app.route('/education')
def education():
    return render_template('education.html', **context, url=os.getenv("URL"))