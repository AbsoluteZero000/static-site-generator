from leafnode import LeafNode
from textnode import TextNode
import re
from htmlnode import HTMLNode
from md_to_text_node import *
from copystatic import copy_files_recursive
import os
import shutil

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

def extract_title(markdown):
    return markdown.split("\n", 1)[0][2:].trim()


def text_to_textnodes(text):
    # initalizes a list of TextNodes     [testesjkjsd;alkfjsdjf, "text"]  (** bold **, "bold") (jasdfljk;adsjfkasd, "text")
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
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = blocks_to_block_type(block)
        node = None
        match(block_type):
            case "heading":
                node = HTMLNode(f"h{len(block.split()[0])}", block)
            case "paragraph":
                node = HTMLNode("p", block)
            case "unordered_list":
                node = HTMLNode("ul", None, [HTMLNode("li", line) for line in block.split("\n")])
            case "ordered_list":
                node = HTMLNode("ol", None, [HTMLNode("li", line) for line in block.split("\n")])
            case "code":
                node = HTMLNode("code", block)
            case "quote":
                node = HTMLNode("blockquote", block)
            case _:
                raise ValueError("This is not a valid type of block")
        nodes.append(node)
    return HTMLNode("div", None, nodes)





def generate_page(from_path, template_path, dest_path):
    with open(from_path, "r") as f:
        markdown = f.read()



dir_path_static = "./static"
dir_path_public = "./public"


def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    copy_files_recursive(dir_path_static, dir_path_public)

main()
