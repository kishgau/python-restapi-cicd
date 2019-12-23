#!/usr/bin/env python
from flask import Flask

webapp = Flask(__name__)


@webapp.route('/')
@webapp.route('/adt/')
def entry_splash_():
    return 'ASX daily average turnover!'


@webapp.route('/adt/<ticker>/')
def get_adt(ticker):
    return 'ADT for %s!\n' % ticker


if __name__ == '__main__':
    webapp.run(host='0.0.0.0')  # open for everyone
