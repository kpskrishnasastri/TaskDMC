from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

API_KEY = "your_api_key_here"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Movie Search</title>
</head>
<body>
    <h2>Search for a Movie</h2>
    <form method="GET">
        <input type="text" name="movie">
        <button type="submit">Search</button>
    </form>
    {% if title %}
    <div>
        <h3>{{ title }}</h3>
        <img src="{{ poster }}" width="200">
        <p>{{ year }}</p>
    </div>
    {% endif %}
</body>
</html>
"""

