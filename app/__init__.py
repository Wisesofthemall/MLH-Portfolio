import os
from flask import Flask, redirect, render_template, request, url_for, abort
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
import re

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                        user=os.getenv("MYSQL_USER"),
                        password=os.getenv("MYSQL_PASSWORD"),
                        host=os.getenv("MYSQL_HOST"),
                        port=3306
                        )

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/')
def index():
    return render_template('index.html',  url=os.getenv("URL"))

@app.route('/about')
def about():
    return render_template('about.html',  url=os.getenv("URL"))

@app.route('/work')
def work():
    return render_template('work.html',  url=os.getenv("URL"))

@app.route('/hobby')
def hobby():
    return render_template('hobby.html',  url=os.getenv("URL"))

@app.route('/education')
def education():
    return render_template('education.html',  url=os.getenv("URL"))

@app.route('/place')
def place():
    return render_template('place.html', url=os.getenv("URL"))

def navbar():
    return render_template('navbar.html',  url=os.getenv("URL"))

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    
    # regex for email validation
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    name = request.form.get('name')
    email = request.form.get('email')
    content = request.form.get('content')

    # Validate name
    if not name:
        abort(400, description="Invalid name")

    # Validate email
    if not email or not re.match(email_regex, email):
        abort(400, description="Invalid email")

    # Validate content
    if not content:
        abort(400, description="Invalid content")

    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return redirect(url_for('timeline'))

@app.route('/timeline')
def timeline():
    posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    return render_template('timeline.html', timeline_posts=posts, title="Timeline")
