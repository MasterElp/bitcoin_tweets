from flask import Flask, render_template, redirect, url_for, request
from datetime import date
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, IntegerField
from wtforms import TextAreaField, validators
#from wtforms.ext.dateutil.fields import DateTimeField
from wtforms.fields.simple import TextField


app = Flask(__name__)

app.config['SECRET_KEY']='asdf45bgdDDr3w5gDfwf'

class MainForm(FlaskForm):
    tweet_text = TextAreaField('Tweet text', [validators.required(), validators.length(max=100)])
    #retweets = IntegerField('Retweets', default=0)
    #tweet_datetime = DateTimeField('Tweet time')

    #def validate_on_submit(self):
    #        result = super(MainForm, self).validate()
    #        if (self.startdate.data>self.enddate.data):
    #            return False
    #        else:
    #            return result


messages = []


@app.route('/', methods=['GET','POST'])
def index():
    error=''
    main_form = MainForm()
    if main_form.validate_on_submit():
        messages.append('Text is : {} '.format(main_form.tweet_text.data))
    else:
        if main_form.is_submitted():
            error = "max 100"

    return render_template('index.html', form=main_form, messages=messages, error = error)
    main_form.proccess()

    #return render_template('index.html', messages=messages, form=main_form, error=error)




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')