from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, IntegerField
from wtforms import TextAreaField, validators
#from wtforms.ext.dateutil.fields import DateTimeField
from wtforms.fields.simple import TextField

from app import constants, controllers

class MainForm(FlaskForm):
    tweet_text = TextAreaField('Tweet text', [validators.required()])#, validators.length(max=constants.TWEETS_MAX_LENGHT)
    #retweets = IntegerField('Retweets', default=0)
    #tweet_datetime = DateTimeField('Tweet time')

    def validate_on_submit(self):
            result = super(MainForm, self).validate()

            bert_model = controllers.BertModelEmbendibg()
            bert_model.set_text(self.tweet_text.data)

            if (bert_model.get_token_lenght() > constants.TOKENS_MAX_LENGHT):
                return False
            else:
                return result