import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.info import context
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

"""
    View function for each route. (e.g. /, /about, /work, /hobby, /education, /place)

    Renders the html template with the 'context' dictionary and the 'URL' environment variable.

    Returns:
        Rendered HTML template.
"""

# Define routes and corresponding view functions
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

@app.route('/place')
def place():
    return render_template('place.html', **context, url=os.getenv("URL"))

def navbar():
    return render_template('navbar.html', **context, url=os.getenv("URL"))

@app.route('/timeline_post', methods = ['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/timeline_post', methods=['GET'])
def get_time_line_post():
    return{
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")