# import Flask module from flask package
from flask import Flask

# import os module for accessing environment variables
import os

# create a new instance of the Flask application
app = Flask(__name__)

# define a route for the default homepage of the application
@app.route("/")
def index():
   # retrieve the value of the "COLOR_ENV" environment variable
   env_var = os.environ.get("COLOR_ENV")
   # return a string that includes the value of the "COLOR_ENV" environment variable
   return f"Hey {env_var}!"

# start the application on port 5000 if this script is being run directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
