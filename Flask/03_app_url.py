### Building URL dynamically
#### Variable rules and URL Building

from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to my journey of learning flask."

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and marks is "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and marks is "+ str(score)

@app.route('/result/<int:score>')
def result(score):
    if (score>50):
        result = "Pass"
    else:
        result = "Fail"
    return result
if __name__ == '__main__':
    app.run(debug=True)
