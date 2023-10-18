import unittest
from rearrange import rearrange_name  # Ensure to import the rearrange_name function from the correct module

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)    
        
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_one_name(self):
        testcase = "Shima"
        expected = "Shima"
        self.assertEqual(rearrange_name(testcase), expected) 
        
unittest.main()   
