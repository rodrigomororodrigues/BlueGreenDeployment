from flask import Flask, render_template, redirect, url_for, request
import os
PORT = 80
#MESSAGE = "BlueGreen Deployment BRASKEM \n"

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')
#    result = MESSAGE.encode("utf-8")
#    return result
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)