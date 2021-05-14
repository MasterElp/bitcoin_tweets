from flask import Flask, render_template, redirect, url_for, request
from collections import namedtuple
app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []


@app.route('/')
def index():
    return render_template('index.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    messages.append(Message(text, tag))

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')