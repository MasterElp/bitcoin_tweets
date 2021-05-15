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
    model = controllers.BertModelClassificate(main_form.tweet_text.data)
    
    if main_form.validate_on_submit():
        messages.append(model.get_token())
    else:
        if main_form.is_submitted():
            error = "Token lenght {}. Max {} required.".format(model.get_token_lenght(), constants.TOKENS_MAX_LENGHT)

    return render_template('index.html', form=main_form, messages=messages, error=error)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')