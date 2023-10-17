from rearrange import rearrange_name 
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
        
#if __name__ == '__main__':  #added by chatGPT :block to ensure that the test suite is executed only when the script is run directly, not when imported as a module.
     #unittest.main()
     
unittest.main()