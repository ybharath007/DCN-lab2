from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    date = datetime.now()
    return str(date)


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
