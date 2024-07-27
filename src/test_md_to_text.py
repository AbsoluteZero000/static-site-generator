import unittest
from md_to_text_node import *
from textnode import TextNode
from main import *

class TestTextToHTML(unittest.TestCase):
    def test_textmd_to_text_node(self):
        md_node = TextNode("Hello world", "text")
        node = split_nodes_delimiter(md_node, "", "text")
        self.assertEqual(node.text, md_node.text)
    def test_md_to_text_node(self):
        md = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_output = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode(
                "to youtube", "link", "https://www.youtube.com/@bootdotdev"
                )
        ]
        self.assertEqual(expected_output, text_to_textnodes(md))

    def test_md_to_text_blocks(self):
        markdown = """
        # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

        blocks = markdown_to_blocks(markdown)
        self.assertEqual(["# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
"""* This is the first list item in a list block
* This is a list item
* This is another list item"""],            blocks)

    def test_text_blocks_to_types(self):
        blocks = ["# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
"""* This is the first list item in a list block
* This is a list item
* This is another list item"""]
        self.assertEqual("heading", blocks_to_block_type(blocks[0]))
        self.assertEqual("paragraph", blocks_to_block_type(blocks[1]))
        self.assertEqual("unordered_list", blocks_to_block_type(blocks[2]))
if __name__ == "__main__":
    unittest.main()
