from flask import Flask,render_template,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import BooleanField,SelectField,RadioField,TextAreaField,StringField,SubmitField
from wtforms.validators import DataRequired

app=Flask(__name__)
app.config['SECRET_KEY']='monish123'

class Form_func(FlaskForm):
    breed=StringField(label='Enter your breed you dog ? ',validators=[DataRequired()])
    is_veg=RadioField(label='Are you vegan?',choices=[('choice1','Yes'),('choice2','No')])
    mood=SelectField(label='Select your mood',choices=[('mood1','happy'),('mood2','great')])
    review=TextAreaField()
    submit=SubmitField('Submit')

@app.route('/',methods=["GET","POST"])
def index():
    form_obj=Form_func()
    if form_obj.validate_on_submit():
    
        session['breed']=form_obj.breed.data
        session['isvegan']=form_obj.is_veg.data
        session['mood']=form_obj.mood.data
        session['review']=form_obj.review.data
        # form_obj.hidden_tag()
        # form_obj.breed.label
        return redirect(url_for('thankyou'))
    return render_template('index.html',form_obj=form_obj)

@app.route('/thanyou')
def thankyou():
    return render_template('thankyou.html')
if __name__ == "__main__":
    app.run(debug=True)
