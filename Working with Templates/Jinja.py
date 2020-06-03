from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def show_details():
    name='monish'
    list_name=list(name)
    dictionary={'name':'Monish'}
    return render_template('Jinja.html',name=name,list_name=list_name,dictionary=dictionary)

if __name__ == "__main__":
    app.run(debug=True)