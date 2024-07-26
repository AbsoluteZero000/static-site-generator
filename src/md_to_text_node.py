from textnode import TextNode
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if(text_type == "text"):
        return old_nodes
    for node in old_nodes:
        if(node.text_type != "text"):
            new_nodes.append(node)
            continue
        new_text = node.text.split(delimiter)
        if(len(new_text)%2 == 0):
            raise Exception("each opening delimiter must have a closing delimiter")
        is_normal_text = True
        for text in new_text:
            new_nodes.append(TextNode(text, "text" if is_normal_text else text_type))
            is_normal_text = not is_normal_text
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
# Refactor those two functions
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        extracted_images = extract_markdown_images(node.text)
        if(len(extracted_images) == 0):
            new_nodes.append(node)
            continue
        global_text = node.text
        for image in extracted_images:
            sections = global_text.split(f"![{image[0]}]({image[1]})", 1)
            if(sections[0] != ""):
                new_nodes.append(TextNode(sections[0], "text"))
            new_nodes.append(TextNode(image[0], "image", image[1]))
            global_text = sections[1]
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        extracted_links = extract_markdown_links(node.text)
        if(len(extracted_links) == 0):
            new_nodes.append(node)
            continue
        global_text = node.text
        for link in extracted_links:
            sections = global_text.split(f"[{link[0]}]({link[1]})", 1)
            if(sections[0] != ""):
                new_nodes.append(TextNode(sections[0], "text"))
            new_nodes.append(TextNode(link[0], "link", link[1]))
            global_text = sections[1]
    return new_nodes
