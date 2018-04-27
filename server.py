from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Soon, pretty D3 charts!'

if __name__ == '__main__':
    app.run()
