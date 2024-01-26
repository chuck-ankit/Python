##Integrate HTML from flask
## HTTP verb GET and POST

#Jinja2 Techniques

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('05_index.html')

if __name__ == '__main__':
    app.run(debug=True)
