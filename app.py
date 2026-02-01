from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    return "<h1>Network Health Analyzer Running!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

