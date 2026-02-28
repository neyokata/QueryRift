# test_queryrift.py
"""
Tests for QueryRift module.
"""

import unittest
from queryrift import QueryRift

class TestQueryRift(unittest.TestCase):
    """Test cases for QueryRift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QueryRift()
        self.assertIsInstance(instance, QueryRift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QueryRift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
