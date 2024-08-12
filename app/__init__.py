"""
This module initializes the Flask application and defines the view functions
for various routes.

Routes:
    /deploy: POST route to run CI pipeline and redeploy the site.
    /: GET route to render the index page.
    /about: GET route to render the about page.
    /work: GET route to render the work page.
    /hobby: GET route to render the hobby page.
    /education: GET route to render the education page.
    /place: GET route to render the place page.
    /navbar: GET route to render the navbar (called within templates).

The view functions render the HTML templates with the 'context' dictionary and
the 'URL' environment variable.
"""
import os
import datetime
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv
from playhouse.shortcuts import model_to_dict
from peewee import *
from app.info import context

load_dotenv()

mydb = MySQLDatabase(
    os.getenv('MYSQL_DATABASE'),
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    host=os.getenv('MYSQL_HOST'),
    port=3306
)


class TimelinePost(Model):
    """
    Model class to represent the timeline posts.

    Attributes:
        name (CharField): Name of the post.
        email (CharField): Email of the post.
        content (TextField): Content of the post.
        date (DateTimeField): Date of the post.
    """
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta class to define the database and table for the model.
        """
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost], safe=True)
app = Flask(__name__)
@app.route('/api/timeline', methods=['GET', 'POST', 'DELETE'])
def timeline():
    """
    GET and POST route to fetch and add timeline posts.

    This view function fetches all the timeline posts from the database and
    returns them as a JSON response. It also adds a new post to the database
    if the request method is POST.

    Returns:
        dict: JSON response with the timeline posts.
    """
    if request.method == 'GET':

        return {
            'posts': list(
                map(model_to_dict,
                    TimelinePost.select().order_by(TimelinePost.created_at.desc())
                    )
                ),
        }
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        content = request.form['content']

        post = TimelinePost.create(name=name, email=email, content=content)
        return model_to_dict(post)
    if request.method == 'DELETE':
        i_d  = request.args.get('id')

        post = TimelinePost.get_by_id(i_d)
        post.delete_instance()
        return model_to_dict(post)
    return 'Invalid Request Method ', 405



@app.route('/deploy', methods=['POST'])
def deploy():
    """
    POST route to run the CI pipeline and redeploy the site.

    This view function executes the `run_test.sh` and `redeploy-site.sh` scripts
    to test and redeploy the site. If any script fails, it returns a 500 error.

    Returns:
        str: Deployment status message.
    """
    if request.method == 'POST':
        exit_status = os.system('chmod +x ./run_test.sh && ./run_test.sh')
        if exit_status != 0:
            return 'Error: Failed CI Pipeline ', 500

        exit_status = os.system('chmod +x ./redeploy-site.sh && ./redeploy-site.sh')
        if exit_status != 0:
            return 'Error: Failed Deployment ', 500
        return 'Deployment initiated ', 200
    return 'Invalid Request Method ', 405

# Define routes and corresponding view functions
@app.route('/')
def index():
    """
    GET route to render the index page.

    This view function renders the 'index.html' template with the 'context'
    dictionary and the 'URL' environment variable.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('index.html', **context, url=os.getenv("URL"))

@app.route('/about')
def about():
    """
    GET route to render the about page.

    This view function renders the 'about.html' template with the 'context'
    dictionary and the 'URL' environment variable.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('about.html', **context, url=os.getenv("URL"))

@app.route('/work')
def work():
    """
    GET route to render the work page.

    This view function renders the 'work.html' template with the 'context'
    dictionary and the 'URL' environment variable.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('work.html', **context, url=os.getenv("URL"))

@app.route('/hobby')
def hobby():
    """
    GET route to render the hobby page.

    This view function renders the 'hobby.html' template with the 'context'
    dictionary and the 'URL' environment variable.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('hobby.html', **context, url=os.getenv("URL"))

@app.route('/education')
def education():
    """
    GET route to render the education page.

    This view function renders the 'education.html' template with the 'context'
    dictionary and the 'URL' environment variable.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('education.html', **context, url=os.getenv("URL"))

@app.route('/place')
def place():
    """
    GET route to render the place page.

    This view function renders the 'place.html' template with the 'context'
    dictionary and the 'URL' environment variable.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('place.html', **context, url=os.getenv("URL"))

@app.route('/feed')
def feed():
    """
    Function to render the feed template.

    This function renders the 'feed.html' template with the 'context'
    dictionary and the 'URL' environment variable.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('feed.html', **context, url=os.getenv("URL"))


def navbar():
    """
    Function to render the navbar template.

    This function renders the 'navbar.html' template with the 'context'
    dictionary and the 'URL' environment variable.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('navbar.html', **context, url=os.getenv("URL"))


if __name__ == "__main__":
    app.run(debug=True)