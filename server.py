from flask import Flask, jsonify, render_template

from adapter import get_countries_tree

app = Flask(__name__)

@app.route('/')
def serve_index():
    title = 'Data Viz'
    return render_template('index.html', title=title)

@app.route('/api/countries')
def api():
    res = get_countries_tree()
    return jsonify({ 'data': res })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
