from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>I am monish ostwal.</h1>'
@app.route('/info')
def info():
    return '<h2>I love to code.</h2>'
if __name__ == "__main__":
    app.run()