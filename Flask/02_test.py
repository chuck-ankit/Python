from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Hello Server.Just tyling to learn WSDI conccepts."
    
if __name__ == '__main__':
    app.run(debug==True)
