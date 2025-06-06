import sys
import os

# Add the project directory to the Python path
project_home = os.path.abspath(os.path.join(os.path.dirname(__file__), 'IPL-3.0'))
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variable for Flask app if not already set (optional, but good practice)
# os.environ['FLASK_APP'] = 'app.py' # This is often set in the PythonAnywhere web tab

# Change to the project directory
# PythonAnywhere usually runs the WSGI file from a different directory,
# so scripts and relative paths in your app might need the CWD to be the project root.
os.chdir(project_home)

# Import the Flask app
# The file is IPL-3.0/app.py, and the Flask app instance is named 'app'
from app import app as application

# If you had blueprints or other initializations that need to be explicitly run,
# you might do them here, but typically the import above is enough.
