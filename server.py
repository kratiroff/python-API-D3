from flask import Flask, jsonify
from flask import render_template

from adapter import get_countries_tree

app = Flask(__name__)

@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/api/countries')
def api():
    res = get_countries_tree()
    return jsonify({ 'countries': res })

if __name__ == '__main__':
    app.run(debug=True)
