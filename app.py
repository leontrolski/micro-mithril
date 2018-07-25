import json
import flask

app = flask.Flask(__name__)

@app.route('/')
def root():
    with open('index.html') as f:
        return f.read()


@app.route('/some-data', methods=['POST'])
def some_data():
    print(flask.request.json)
    return json.dumps({'foo': 'bar'})


app.run(debug=True)