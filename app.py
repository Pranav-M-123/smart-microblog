from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the AI Smart Microblog!"

if __name__ == '__main__':
    app.run(debug=True)