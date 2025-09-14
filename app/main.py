# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify, request
from datetime import datetime
# from urllib import request
import argparse
import os

env = os.getenv("environment")

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/healthz')
# ‘/’ URL is bound with hello_world() function.
def healthz():
    return jsonify({"status": "ok", "environment":env}), 200

@app.route('/date')
def date(): 
    today = datetime.now()
    return jsonify({"date": today}), 200


@app.route('/write', methods = ['POST'])
def write():
    if request.is_json:
        data = request.get_json()
        print(data)
        message = data.get("message")
        if message:
            with open("./logs/messages.txt", "a") as file:
                file.write(message + "\n")
    return "ok", 200

# main driver function
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="run flask")
    parser.add_argument("--host",required=False, type=str, help="IP Address such as '0.0.0.0'", default="127.0.0.1")
    parser.add_argument("--port",required=False,type=int, help= "port wher you want to expose the flask app",default=5000)
    args = parser.parse_args()
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host=args.host,port=args.port, debug=True)
    # app.run()