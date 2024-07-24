import unittest
import io
from contextlib import redirect_stdout

from parentnode import ParentNode
from leafnode import LeafNode


"""
testcases that should be tested:
    1- empty constructor
    2- None tag
    3- None children
    4- children empty list
    5- constructor with one parent multiple leaf children 
    6- constructor with parent(parent(leaf))

"""
class TestParentNode(unittest.TestCase):
    
    def test_empty_constructor(self):
        node = ParentNode()
        try:
            node.to_html()
            self.assertTrue(False)
        except ValueError as e:
            self.assertTrue(True)

    def test_none_tag(self):
        node = ParentNode(None, children=[LeafNode("b","hello world")])
        try:
            node.to_html()
            self.assertTrue(False)
        except ValueError as e:
            self.assertTrue(True)
   
    def test_none_children(self):
        node = ParentNode("b", None)
        try:
            node.to_html()
            self.assertTrue(False)
        except ValueError as e:
            self.assertTrue(True)
    
    def test_empty_list_children(self):
        node = ParentNode("b", [])
        try:
            node.to_html()
            self.assertTrue(False)
        except ValueError as e:
            self.assertTrue(True)
   
    def test_constructor(self):
        node = ParentNode("p", [
            LeafNode("b", "This is Bold Text", {"styles":"color: red", "font-size":"16px"}),
            LeafNode("a", "This is a Link"),
            LeafNode("p", "This is a paragraph Text", {"styles":"color: red", "font-size":"16px"}),
            ])
        expected_html = "<p><b styles=\"color: red\" font-size=\"16px\">This is Bold Text</b><a>This is a Link</a><p styles=\"color: red\" font-size=\"16px\">This is a paragraph Text</p></p>"
        self.assertEqual(node.to_html(), expected_html)
    
    def test_constructor_with_three_layers_of_nesting(self):
        node = ParentNode("p", [
            ParentNode("p", [LeafNode("b", "This is Bold Text"),]), 
            ])
        expected_html = "<p><p><b>This is Bold Text</b></p></p>"
        self.assertEqual(node.to_html(), expected_html)
    

if __name__ == "__main__":
    unittest.main()
