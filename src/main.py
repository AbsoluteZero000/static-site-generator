from leafnode import LeafNode
from textnode import TextNode
import re

from md_to_text_node import *

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case "text":
            return LeafNode(value=text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case "image":
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        case _:
            raise ValueError("This is not a valid type of text_node")


def text_to_textnodes(text):
    # initalizes a list of TextNodes
    nodes = [TextNode(text, "text")]
    # splits nodes by delimiters
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    nodes = split_nodes_delimiter(nodes, "`", "code")
    # splits nodes by links and images
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    # returns the list of TextNodes
    return nodes

def markdown_to_blocks(markdown):
    return [block.strip() for block in markdown.split("\n\n") if block != ""] # removes empty blocks

def blocks_to_block_type(block):
    pattern = re.compile(r'^\d+\. ')

    if(block.startswith("#")):
        return "heading"
    if(all(line.startswith("* ") for line in block.split("\n")) or all(line.startswith("- ") for line in block.split("\n"))):
        return "unordered_list"
    if(block.startswith("```") and block.endswith("```")):
        return "code"
    if(block.startswith(">")):
        return "quote"
    if(all(pattern.match(line) for line in block.split("\n"))):
        return "ordered_list"
    return "paragraph"
def main():
    pass
main()
