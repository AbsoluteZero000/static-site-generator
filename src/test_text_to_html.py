import unittest
from main import *
from textnode import TextNode


class TestTextToHTML(unittest.TestCase):
    def test_normal_text_to_html(self):
        node = TextNode("This is a normal paragraph", "text")
        expected_html = "This is a normal paragraph"
        self.assertEqual(expected_html, text_node_to_html_node(node).to_html())

    def test_bold_to_html(self):
        node = TextNode("This is a bold paragraph", "bold")
        expected_html = "<b>This is a bold paragraph</b>"
        self.assertEqual(expected_html, text_node_to_html_node(node).to_html())

    def test_link_to_html(self):
        node = TextNode("This is a link", "link", "https://github.com/AbsoluteZero000")
        expected_html = "<a href=\"https://github.com/AbsoluteZero000\">This is a link</a>"
        self.assertEqual(expected_html, text_node_to_html_node(node).to_html())

    def test_img_to_html(self):
        node = TextNode("This is an img", "image", "https://github.com/AbsoluteZero000/profile_pic")
        expected_html = "<img src=\"https://github.com/AbsoluteZero000/profile_pic\" alt=\"This is an img\"></img>"
        self.assertEqual(expected_html, text_node_to_html_node(node).to_html())

if __name__ == "__main__":
    unittest.main()
