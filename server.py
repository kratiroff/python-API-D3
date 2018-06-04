from flask import Flask, jsonify
from flask import render_template

from adapter import get_anything

app = Flask(__name__)

@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/api/test')
def api():
    res = get_anything()
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)
