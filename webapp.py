#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def entry_splash_():
    return '/adt/ticker : ASX daily average turnover!\ne.g. /adt/BHP'


@app.route('/adt/<ticker>/')
def get_adt(ticker):
    return 'Hello %s!\n' % ticker


if __name__ == '__main__':
    app.run(host='0.0.0.0')  # open for everyone
