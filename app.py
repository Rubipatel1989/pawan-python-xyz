from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
  return "I am the best beacuse I am best and Neha also best"

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)