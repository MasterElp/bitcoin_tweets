from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, IntegerField
from wtforms import TextAreaField, validators
#from wtforms.ext.dateutil.fields import DateTimeField
from wtforms.fields.simple import TextField

class MainForm(FlaskForm):
    tweet_text = TextAreaField('Tweet text', [validators.required(), validators.length(max=100)])
    #retweets = IntegerField('Retweets', default=0)
    #tweet_datetime = DateTimeField('Tweet time')

    #def validate_on_submit(self):
    #        result = super(MainForm, self).validate()
    #        if (self.tweet_text):
    #            return False
    #        else:
    #            return result