import unittest
import io
from contextlib import redirect_stdout

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_constructor(self):
        node = LeafNode("p", "This is a HTML node")
        expected_html = "<p>This is a HTML node</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_constructor_with_props(self):
        node = LeafNode("p", "This is a HTML node", {"href":"http:localhost:8080", "styles":"color:red"})
        expected_html = "<p href=\"http:localhost:8080\" styles=\"color:red\">This is a HTML node</p>"
        self.assertEqual(node.to_html(), expected_html)






if __name__ == "__main__":
    unittest.main()
