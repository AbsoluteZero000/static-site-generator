from leafnode import LeafNode
from textnode import TextNode


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
    nodes = [TextNode(text, "text")]
    for node in nodes:
        print(node)
    print("-------------")
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    for node in nodes:
        print(node)
    print("-------------")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    for node in nodes:
        print(node)
    print("-------------")
    nodes = split_nodes_delimiter(nodes, "`", "code")
    for node in nodes:
        print(node)
    print("-------------")
    nodes = split_nodes_image(nodes)
    for node in nodes:
        print(node)
    print("-------------")

    nodes = split_nodes_link(nodes)
    for node in nodes:
        print(node)
    print("-------------")

    return nodes
def main():
    text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
main()
