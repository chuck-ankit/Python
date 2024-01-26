from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Hello Server.Just trying to learn WSDI conccepts. Testing "
    
if __name__ == '__main__':
    app.run(debug=True)
