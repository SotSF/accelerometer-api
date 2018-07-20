from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/")
def index():
    return app.send_static_file('index.html')

wasFast = False

@app.route("/fast", methods=["GET", "POST"])
def fast():
    global wasFast
    if request.method == 'GET':
        retval = bool(wasFast)
        wasFast = False
        return jsonify(retval)
    wasFast = True
    return jsonify(True)

app.run()