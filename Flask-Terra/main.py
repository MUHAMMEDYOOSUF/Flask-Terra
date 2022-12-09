from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/test",  methods=["GET"])
def test_function():
    """return hii"""
    return "hii"



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4321))
    app.run(debug=True, host='0.0.0.0', port=port)