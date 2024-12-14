# Import the Flask class from the flask package
from flask import Flask

# Create an instance of the Flask class. 
# __name__ is passed to help Flask determine the app's root path.
app = Flask(__name__)

# Define a route for the root URL ('/') and bind it to the hello() function.
@app.route('/')
def hello():
    # This function is executed when a user accesses the root URL.
    # It returns a simple "Hello, world!" message as the response.
    return 'Hello, world!'

# Check if the script is being run directly (not imported as a module).
if __name__ == '__main__':
    # Run the Flask dev
