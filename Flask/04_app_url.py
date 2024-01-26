### Building URL dynamically
#### Variable rules and URL Building
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Hello Server.Just trying to learn building dynamic URL. Testing "


@app.route('/result/<int:marks>')
def result(marks):
    result = "Pass" if marks > 50 else "Fail"
    return render_template('04_result.html', result=result, marks=marks)

if __name__ == '__main__':
    app.run(debug=True)