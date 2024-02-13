"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""
from unittest import TestCase

# we need to import the unit under test - counter
from src.counter import app

# we need to import the file that contains the status codes
from src import status


class CounterTest(TestCase):
    """Counter tests"""
    def setUp(self):
        self.client = app.test_client()
    def test_create_a_counter(self):
        """It should create a counter"""
        result = self.client.post('/counters/foo')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    def test_update_a_counter(self):
        """It should update a counter"""
        result = self.client.post('/counters/foo')
        updatedCounter = self.client.put('/counters/foo')
        self.assertEqual(updatedCounter.status_code, status.HTTP_200_OK)
        self.assertEqual(b'{"foo":1}\n', updatedCounter.data)
        self.assertGreater(updatedCounter.data, result.data)

    def test_read_a_counter(self):
        """It should read a counter"""
        counter = self.client.post('/counters/foo')
        readCounter = self.client.get('counters/foo')
        self.assertEqual(readCounter.status_code, status.HTTP_200_OK)
        self.assertEqual(b'{"foo":0}\n', readCounter.data)

    def test_delete_a_counter(self):
        """It should delete a counter"""
        deleteCounter = self.client.post('/counters/foo')
        #self.assertEqual(deleteCounter.status_code, status.HTTP_200_OK)
        deleteCounter = self.client.delete('/counters/foo')
        self.assertEqual(deleteCounter.status_code, status.HTTP_204_NO_CONTENT)


