from flask import render_template, flash, redirect, url_for
from app import app 
from app.forms import InputForm
from app.did_you_mean import closest_match 


@app.route('/') 
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/form', methods=['GET', 'POST'])
def form_page():
    form = InputForm()
    input_word = form.data['input_word']
    if form.validate_on_submit():
        result = closest_match(input_word)
        flash(result)
    return render_template('form.html', title='Did you mean?', form=form)

