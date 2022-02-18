from flask import Flask
app = Flask(__name__)
# Create flask routes
@app.route('/')
def hello_world():
    return 'Hello world'