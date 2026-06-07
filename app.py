from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>AWS Lightsail Deployment Successful</h1><p>Student: Nandhana</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)