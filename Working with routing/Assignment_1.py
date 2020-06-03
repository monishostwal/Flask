from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'Type /puppy_latin/<name> to see your name in latin'

@app.route('/puppy_latin/<name>')
def latin(name):
    if(name[-1]=='y'):
        name=name[:-1]
        name=name+'ies'
    else:
        name=name+'y'
    return name


if __name__ == "__main__":
    app.run(debug=True)

