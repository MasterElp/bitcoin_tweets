from flask import Flask, render_template, redirect, url_for, request
from datetime import date
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, IntegerField
from wtforms.fields.html5 import DateTimeField
#from wtforms.ext.dateutil.fields import DateTimeField
from collections import namedtuple

from wtforms.fields.simple import TextField
app = Flask(__name__)

app.config['SECRET_KEY']='asdf45bgdDDr3w5gDfwf'

class MainForm(FlaskForm):
    tweet_text = TextField('Tweet text')
    #retweets = IntegerField('Retweets', default=0)
    #tweet_datetime = DateTimeField('Tweet time')
    
    def proccess(self):
        messages.append(Message(self.tweet_text, 'e'))


Message = namedtuple('Message', 'text tag')
messages = []
error = None


@app.route('/', methods=['GET','POST'])
def index():
    
    main_form = MainForm()
    #main_form.proccess()
    
    #text = request.form['text']
    #tag = request.form['tag']

    
    

    return render_template('index.html', messages=messages, form=main_form, error=error)


@app.route('/add_message', methods=['POST'])
def add_message():
    main_form = MainForm()
    main_form.proccess()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')