# -*- coding: utf-8 -*-

import flask
from healthcheck import HealthCheck

HOST = '0.0.0.0'
PORT = 8888
DEBUG = False

app = flask.Flask(__name__)


@app.route('/hello')
def hello():
    return flask.jsonify(message='Hello World')


def healthcheck():
    return True, 'server alive'


health = HealthCheck(app, '/_health/ping')

health.add_check(healthcheck)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
