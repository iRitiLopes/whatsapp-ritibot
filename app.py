# flask application
from flask import Flask, render_template, request, Response
from flask_ngrok import run_with_ngrok
import os

ENV = os.getenv('ENV', 'development')
app = Flask(__name__)


if ENV == 'development':
    print('running with ngrok')
    run_with_ngrok(app)


@app.get('/')
@app.get('/<name>')
def hello(name=None):
    return request.args.get("hub.challenge", "xd")


# flask post method called handler and receive a body from whatsapp webhook
@app.post('/')
def handler():
    # get body from whatsapp webhook
    body = request.get_json()
    # print body
    print(body)
    # return response
    return Response(status=200)


if __name__ == "__main__":
    # run flask app
    if ENV == 'development':
        app.run()
    else:
        app.run(debug=True, host="0.0.0.0", port=5000)
