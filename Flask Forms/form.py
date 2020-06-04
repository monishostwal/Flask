from flask import Flask,render_template
from flask_wtf import  FlaskForm
from wtforms import StringField,SubmitField

app=Flask(__name__)
app.config['SECRET_KEY']='monish123'

class Info(FlaskForm):
    breed=StringField(label="Enter your Breed?")
    submit=SubmitField(label='Submit Name')

@app.route('/',methods=['GET','POST'])
def index():
    breed=False
    info_obj=Info()
    if(info_obj.validate_on_submit):
        breed=info_obj.breed.data
        info_obj.breed.data=''
        # info_obj.breed.label
        # info_obj.breed.data
    return render_template('form.html',breed=breed,info_obj=info_obj)
if __name__ == "__main__":
    app.run(debug=True)
