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
        

# if __name__ == '__main__':
 #    unittest.main()
    
    
unittest.main()   
