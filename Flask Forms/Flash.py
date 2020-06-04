from flask import Flask,render_template,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import SubmitField

app=Flask(__name__)

app.config['SECRET_KEY']='nikl'

class Show(FlaskForm):
    submit=SubmitField('Show Flash')

@app.route('/',methods=['GET','POST'])
def index():
    show=Show()
    if show.validate_on_submit():
        flash('Clicked on me')
        print("AAYA")
        return redirect(url_for('index'))
    return render_template('flash.html',show=show)
if __name__ == "__main__":
    app.run(debug=True)