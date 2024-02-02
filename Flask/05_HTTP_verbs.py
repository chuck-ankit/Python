from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks < 50:
        result = 'Fail'
    else:
        result = 'Pass'
    return render_template('05_result.html', result=result)

@app.route('/')
def welcome():
    return render_template('05_index.html')

@app.route('/Pass/<int:marks>')
def success(marks):
    return "<html><body>The Result is Pass and the marks are " + str(marks) + "</body></html>"

@app.route('/Fail/<int:marks>')
def fail(marks):
   return "<html><body>The Result is Fail and the marks are " + str(marks) + "</body></html>"

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        if 'Science' in request.form and 'Maths' in request.form and 'Data_Science' in request.form:
            science = float(request.form['Science'])
            maths = float(request.form['Maths'])
            datascience = float(request.form['Data_Science'])
            total_score = (science + maths + datascience) / 3
        else:
            return "Invalid form data. Please make sure all required fields are filled."
    res = ""
    if total_score < 50:
        res = "Fail"
    else:
        res = "Pass"
    return redirect(url_for('result', marks=total_score))

if __name__ == '__main__':
    app.run(debug=True)
