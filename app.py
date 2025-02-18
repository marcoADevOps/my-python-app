from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, GitOps! This is my Python app running on Kubernetes.Now you are seeing the version 2 of this application"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
