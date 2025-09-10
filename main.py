# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify
from datetime import datetime
import argparse

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/healthz')
# ‘/’ URL is bound with hello_world() function.
def healthz():
    return jsonify({"status": "ok"}), 200

@app.route('/date')
def date(): 
    today = datetime.now()
    return jsonify({"date": today}), 200

# main driver function
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="run flask")
    parser.add_argument("host",type=str, help="IP Address such as '0.0.0.0'", default="0.0.0.0")
    parser.add_argument("port",type=int, help= "port wher you want to expose the flask app",default=5000)
    args = parser.parse_args()
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host=args.host,port=args.port)
    # app.run(host="0.0.0.0")