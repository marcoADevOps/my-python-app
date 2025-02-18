from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, GitOps! This is my Python app running on Kubernetes.This is a update"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
