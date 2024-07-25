import unittest
import io
from contextlib import redirect_stdout
from md_to_text_node import *
from textnode import TextNode


class TestTextToHTML(unittest.TestCase):
    def test_textmd_to_text_node(self):
        md_node = TextNode("Hello world", "text")
        node = split_nodes_delimiter(md_node, "", "text")
        self.assertEqual(node.text, md_node.text)

if __name__ == "__main__":
    unittest.main()
