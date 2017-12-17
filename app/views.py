from flask import Flask

# Create App
app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def home():
	return '<h1>Hello, Paul</h1>'