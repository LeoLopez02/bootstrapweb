from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods="['GET']")
def index():
  return app.send_static_file('index.html')