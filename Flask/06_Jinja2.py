from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)