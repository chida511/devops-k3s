from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask on Kubernetes with Helm and GitHub Actions!"
