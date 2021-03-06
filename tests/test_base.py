import os
import sys
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import ravendb
import os

class TestCase(unittest.TestCase):

    def get_store(self):
        uri = os.environ['ravenhq_url']
        db = os.environ['ravenhq_db']
        apikey = os.environ['ravenhq_apikey']
        return ravendb.store(uri, db, apikey)

    def get_uri(self):
        return os.environ['ravenhq_url']

    def get_db(self):
        return os.environ['ravenhq_db']
