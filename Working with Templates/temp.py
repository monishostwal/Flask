from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def show():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run()