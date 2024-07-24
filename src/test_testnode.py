import unittest
import io
from contextlib import redirect_stdout

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is not a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
   
    def test_not_eq_text_type(self):
        node = TextNode("This is not a text node", "bold")
        node2 = TextNode("This is not a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_str(self):
        node = TextNode("This is a text node", "bold")
        expected_output = "TextNode(This is a text node, bold, None)"
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
              print(node) 

        output = captured_output.getvalue().strip()

        self.assertEqual(output, expected_output) 



if __name__ == "__main__":
    unittest.main()
