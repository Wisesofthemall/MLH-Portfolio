import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.info import context
import time
load_dotenv()
app = Flask(__name__)


"""
    View function for each route. (e.g. /, /about, /work, /hobby, /education, /place)

    Renders the html template with the 'context' dictionary and the 'URL' environment variable.

    Returns:
        Rendered HTML template.
"""
# Deploy route to check any changes in the repository
@app.route('/deploy', methods=['POST'])
def deploy():
    if request.method == 'POST':
        exit_status = os.system('chmod +x ./run_test.sh && ./run_test.sh')
        if exit_status != 0:
            return f'Error: Failed CI Pipeline ', 500

        exit_status = os.system('chmod +x ./redeploy-site.sh && ./redeploy-site.sh')
        if exit_status != 0:
            return f'Error: Failed Deployment ', 500
        return f'Deployment initiated ', 200

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

def map():
    return render_template('map.html', **context, url=os.getenv("URL"))

if __name__ == "__main__":
    app.run(debug=True)