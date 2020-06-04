from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check():
    lower_case_letter=False
    upper_case_letter=False
    number_end=False
    username=request.args.get('username')
    upper_case_letter=any(c.isupper() for c in username)
    lower_case_letter=any(c.islower() for c in username)
    number_end=username[-1].isdigit()
    result=upper_case_letter and lower_case_letter and number_end
    return render_template('check.html',username=username,upper_case_letter=upper_case_letter,lower_case_letter=lower_case_letter,number_end=number_end,result=result)
if __name__ == "__main__":
    app.run(debug=True)