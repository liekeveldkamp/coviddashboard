# Import the object Flask from the flask module
from flask import Flask

# Create a webserver object called 'COVID Dashboard' and keep track of it in the variable called server
server = Flask('COVID Dashboard')

# Define an HTTP route / to serve the dashboard home web page
@server.route('/')
# Define the function 'index()' and connect it to the route /
def index():
# Return the string "A nice COVID dashboard."
  return "A nice COVID dashboard"

# Define an HTTP route /summary to serve the summary chart
@server.route('/summary')
# Define the function 'serve_summary()' and connect it to the route /summary
def serve_summary():
# Return the string "A bar chart summary of COVID cases per country."
  return "A bar chart summary of COVID cases per country"

# Define an HTTP route /new to serve the new count worldwide chart
@server.route('/new')
# Define the function 'serve_summary_new()' and connect it to the route /new
def serve_summary_new():
# Return the string "A pie chart summary of new COVID cases globally."
  return "A pie chart summary of new COVID cases globally"

# Define an HTTP route /netherlands to serve the chart of the Netherlands
@server.route('/netherlands')
# Define the function 'serve_netherlands_history()' and connect it to the route /netherlands
def serve_netherlands_history():
# Return the string "An area chart of COVID cases over time in the Netherlands."
  return "An area chart of COVID cases over time in the Netherlands"

# Start the webserver
server.run('0.0.0.0')