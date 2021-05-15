from flask import Flask, render_template, redirect, url_for, request
#from datetime import date


from app import controllers, forms

app = Flask(__name__)
app.config['SECRET_KEY']='asdf45bgdDDr3w5gDfwf'



@app.route('/', methods=['GET','POST'])
def index():
    messages = []
    error = None

    main_form = forms.MainForm()
    if main_form.validate_on_submit():
        messages.append(controllers.get_token(main_form.tweet_text.data))
    else:
        if main_form.is_submitted():
            error = "Lenght {}. Max 100 required.".format(len(main_form.tweet_text.data))

    return render_template('index.html', form=main_form, messages=messages, error=error)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')