
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application
app = Flask(__name__)

# Sample data objects
destinations = [
    {"name": "Toronto", "description": "Canada's largest city, known for its CN Tower and diverse culture."},
    {"name": "Vancouver", "description": "A coastal city surrounded by mountains and ocean, known for its Stanley Park and Granville Island."},
    {"name": "Montreal", "description": "A French-speaking city known for its historic Old Town and vibrant arts scene."},
    {"name": "Quebec City", "description": "A charming walled city with European-style architecture and cobblestone streets."},
    {"name": "Ottawa", "description": "Canada's capital city, home to Parliament Hill and the Canadian Museum of History."},
]

activities = [
    {"name": "Niagara Falls", "description": "Visit the iconic瀑布, one of the world's most famous natural wonders."},
    {"name": "CN Tower", "description": "Ascend the tallest free-standing structure in the Western Hemisphere for panoramic views."},
    {"name": "Stanley Park", "description": "Explore a vast urban park with towering trees, beaches, and the Seawall promenade."},
    {"name": "Old Town Montreal", "description": "Step back in time and wander through the historic streets of Montreal's oldest neighborhood."},
    {"name": "Parliament Hill", "description": "Visit the seat of the Canadian government and admire its impressive architecture."},
]

# Define the main route
@app.route('/')
def index():
    return render_template('index.html', destinations=destinations, activities=activities)

# Define the search route
@app.route('/search', methods=['POST'])
def search():
    # Get user input
    destination = request.form.get('destination')
    activity = request.form.get('activity')

    # Filter destinations and activities based on user input
    filtered_destinations = [d for d in destinations if d['name'].lower() == destination.lower()]
    filtered_activities = [a for a in activities if a['name'].lower() == activity.lower()]

    # Redirect to results page
    return redirect(url_for('results', destinations=filtered_destinations, activities=filtered_activities))

# Define the results route
@app.route('/results')
def results():
    # Get destinations and activities from query parameters
    destinations = request.args.getlist('destinations')
    activities = request.args.getlist('activities')

    # Render results page
    return render_template('results.html', destinations=destinations, activities=activities)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
