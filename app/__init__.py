import os
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

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

@app.route('/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return redirect(url_for('timeline'))

@app.route('/timeline')
def timeline():
    posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    return render_template('timeline.html', timeline_posts=posts, title="Timeline")
