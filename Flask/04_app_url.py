### Building URL dynamically
#### Variable rules and URL Building
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello Server. Just trying to learn building dynamic URL. Testing"

@app.route('/result/<int:marks>')
def result(marks):
    result = "Pass" if marks > 50 else "Fail"
    return render_template('04_result.html', result=result, marks=marks)

### Result checker html page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        # Get form data
        marks = int(request.form['marks'])
        
        # Perform some processing
        result = "Pass" if marks > 50 else "Fail"

        # Render the result template with the calculated result
        return render_template('04_result.html', result=result, marks=marks)
    else:
        # If the request is not a POST request, just render the form
        return render_template('submit_form.html')  # Replace 'submit_form.html' with the actual name of your form template

if __name__ == '__main__':
    app.run(debug=True)
