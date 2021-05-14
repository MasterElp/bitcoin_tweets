from flask import Flask, render_template, redirect, url_for, request
from datetime import date
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, IntegerField
from wtforms.fields.html5 import DateTimeField
from collections import namedtuple

from wtforms.fields.simple import TextField
app = Flask(__name__)

app.config['SECRET_KEY']='asdf45bgdDDr3w5gDfwf'

class TestForm(FlaskForm):
    tweet_text = TextField('Tweet text')
    retweets = IntegerField('Retweets', default=0)
    tweet_datetime = DateTimeField('Tweet time')
    start_date = DateField('Start Date', default=date.today)
    end_date = DateField('End Date', default=date.today)

    def validate_on_submit(self):
        result = super(TestForm, self).validate()
        if (self.start_date.data>self.end_date.data):
            return False
        else:
            return result

Message = namedtuple('Message', 'text tag')
messages = []



@app.route('/', methods=['GET','POST'])
def index():
    error = None
    form = TestForm()

    if form.validate_on_submit():
        return 'Start Date is : {} End Date is : {}'.format(form.start_date.data, form.end_date.data)
    else:
        error = "Start date is greater than End date"
    
    #text = request.form['text']
    #tag = request.form['tag']

    messages.append(Message(form.tweet_text, form.tweet_datetime))

    return render_template('index.html', messages=messages, form=form, error=error)


@app.route('/add_message', methods=['POST'])
def add_message():
    

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')