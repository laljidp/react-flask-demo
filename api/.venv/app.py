from flask import Flask
import time
import os

app = Flask(__name__)
SECRET_KEY = os.environ.get('SECRET_KEY') or 'thi$i$s@cr@t'
print(SECRET_KEY)
app.config['SECRET_KEY'] = SECRET_KEY

print(f'__name__ variable::{__name__}')

@app.route('/', methods = ['GET'])
def index():
    return { 'status': 'Your app is running!' }

@app.route('/time')
def get_current_time():
    return { 'time': time.time() }