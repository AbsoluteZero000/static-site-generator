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
        # this is wrong I should match the exact thing
        new_text = ")".join(node.text.split('!')).split(')')
        if(len(new_text) == 1):
            new_nodes.append(node)
            continue
        if(len(new_text)%2 == 0):
            raise Exception("each opening delimiter must have a closing delimiter")
        is_normal_text = True
        images_in_text = extract_markdown_images(node.text)
        i = 0
        for text in new_text:
            if(is_normal_text):
                if len(text) == 0:
                    continue
                new_nodes.append(TextNode(text, "text"))
            else:
                new_nodes.append(TextNode(images_in_text[i][0], "image", images_in_text[i][1]))
                i += 1
            is_normal_text = not is_normal_text
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        # this is wrong as well I should match the exact thing
        new_text = ")".join(node.text.split('[')).split(')')
        if(len(new_text) == 1):
            new_nodes.append(node)
            continue
        if(len(new_text)%2 == 0):
            raise Exception("each opening delimiter must have a closing delimiter")
        is_normal_text = True
        links_in_text = extract_markdown_links(node.text)
        i = 0
        for text in new_text:
            if(is_normal_text):
                if len(text) == 0:
                    continue
                new_nodes.append(TextNode(text, "text"))
            else:
                new_nodes.append(TextNode(links_in_text[i][0], "link", links_in_text[i][1]))
                i += 1
            is_normal_text = not is_normal_text

    return new_nodes
