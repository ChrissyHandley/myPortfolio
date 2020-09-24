from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/work')
def work():
    return render_template('generic.html') 

@app.route('/about')
def about():
    return render_template('elements.html')       

@app.route('/explore')
def explore():
	return 'Places I\'ve explored'

@app.route('/explore/salt_springs')
def explore_salt_springs():
	return 'This is Salt Springs'