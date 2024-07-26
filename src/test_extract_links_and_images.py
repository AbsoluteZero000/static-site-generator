import unittest
import io
from contextlib import redirect_stdout
from main import *
from md_to_text_node import *


class TestExtractMarkdownImagesLinks(unittest.TestCase):

    def test_extract_normal_image(self):
        self.assertEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"))
  
    def test_extract_nomral_link(self):
        self.assertEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"))
    
    def test_extract_link_from_text_node(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text"
            )
        nodes = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode(
                "to youtube", "link", "https://www.youtube.com/@bootdotdev"
                )
            ]
        self.assertEqual(nodes, split_nodes_link([node]))

    def test_extract_image_from_text_node(self):
        node = TextNode(
            "This is text with an image ![image description](https://www.example.com/image.jpg)",
            "text"
        )

        nodes = [
            TextNode("This is text with an image ", "text"),
            TextNode("image description", "image", "https://www.example.com/image.jpg")
        ]

        self.assertEqual(nodes, split_nodes_image([node]))

if __name__ == "__main__":
    unittest.main()



