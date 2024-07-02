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
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.info import context
load_dotenv()
app = Flask(__name__)

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
