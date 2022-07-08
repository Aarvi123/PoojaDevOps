import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to all!"

@app.route('/iiht')
def iiht():
    return 'Welcome to IIHT'
    
@app.route('/duratech')
def dura():
    return 'Welcome to Duratech Solutions, Coimbatore'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
