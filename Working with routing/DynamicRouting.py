from flask import Flask

app=Flask(__name__)

@app.route('/<name>')
def homepage(name):
    string='hello ' +name
    return string+'1'

if __name__ == "__main__":
    app.run(debug=True)