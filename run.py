from flask import Flask, render_template, redirect, url_for, request
#from datetime import date


from app import controllers, forms, constants

app = Flask(__name__)
app.config['SECRET_KEY']='asdf45bgdDDr3w5gDfwf'



@app.route('/', methods=['GET','POST'])
def index():
    messages = []
    error = None

    main_form = forms.MainForm()
    bert_model = controllers.BertModelEmbendibg()
    
    if (main_form.tweet_text.data != None):
        bert_model.set_text(main_form.tweet_text.data)
        if main_form.validate_on_submit(): 
            messages.append(bert_model.get_last_hidden_layers())
        else:
            error = "Token lenght {}. Max {} required.".format(bert_model.get_token_lenght(), constants.TOKENS_MAX_LENGHT)

    return render_template('index.html', form=main_form, messages=messages, error=error)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')