#!/usr/bin/env python
import unittest
import webapp

class TestADT(unittest.TestCase):

    def setUp(self):
        webapp.webapp.testing = True
        self.webapp = webapp.webapp.test_client()

    def test_hello(self):
        rv = self.webapp.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'ASX daily average turnover!')

    def test_adt_calculator(self):
        rv = self.webapp.get('/adt/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'ASX daily average turnover!')

#    def test_adt_calc(self):
#        name = 'TLS'
#        rv = self.webapp.get(f'/adt/{name}')
#        self.assertEqual(rv.status, '200 OK')
  #      self.assertIn(bytearray("{name}", 'utf-8'), rv.data)

if __name__ == '__main__':
    unittest.main()
