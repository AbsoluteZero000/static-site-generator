import unittest
import io
from contextlib import redirect_stdout

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_constructor(self):
        node = HTMLNode("p", "This is a HTML node")
        
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a HTML node")



    def test_str(self):
        node = HTMLNode("h1", "This is a text node")
        node.props = {}
        node.props["target"] = "whatever"
        expected_output = """tag = h1
value = This is a text node
children = None
props = {'target': 'whatever'}"""

        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
              print(node)

        output = captured_output.getvalue().strip()

        self.assertEqual(output, expected_output)



if __name__ == "__main__":
    unittest.main()

