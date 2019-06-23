from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import InputForm

@app.route('/') 
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/form', methods=['GET', 'POST'])
def form_page():
    form = InputForm()
    input_word = form.data['input_word']
    if form.validate_on_submit():
        flash(f'Did you mean {input_word}?')
        #return redirect(url_for('form_page'))
    return render_template('form.html', title='Did you mean?', form=form)

