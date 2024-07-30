import os
from leafnode import LeafNode
from md_to_text_node import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode
from parentnode import ParentNode

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
    return markdown.split("\n", 0)[0][2:].strip()


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
    return [block.strip() for block in markdown.split("\n\n") if block != ""]

def block_to_block_type(block):
    lines = block.split("\n")
    if(block.startswith("# ") or
        block.startswith("## ") or
        block.startswith("### ") or
        block.startswith("#### ") or
        block.startswith("##### ") or
        block.startswith("###### ")
    ):
        return "heading"

    if(all(line.startswith("* ") for line in block.split("\n")) or all(line.startswith("- ") for line in block.split("\n"))):
        return "unordered_list"

    if(lines[-1].startswith("```") and lines[-1].endswith("```")):
        return "code"

    if(block.startswith(">")):
        for line in lines:
            if not line.startswith(">"):
                return "paragraph"
        return "quote"

    if(block.startswith("1. ")):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered_list"
    return "paragraph"

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def heading_to_html_node(block):
    header_level = len(block.split()[0])
    text = " ".join(block.split()[0:])
    children = text_to_children(text[header_level+1:])
    return ParentNode(f"h{header_level}", children)

def paragraph_to_html_node(block):
    return ParentNode("p", text_to_children(" ".join(block.split("\n"))))

def unordered_list_to_html_node(block):
    lines = block.split("\n")
    if(block.startswith("* ")):
        for line in lines:
            if not line.startswith("* "):
                raise Exception("This is not a valid unordered list")
    if(block.startswith("- ")):
        for line in lines:
            if not line.startswith("- "):
                raise Exception("This is not a valid unordered list")

    children = []
    for line in lines:
        child = ParentNode("li", text_to_children(line[1:].strip()))
        children.append(child)
    return ParentNode("ul", children)

def ordered_list_to_html_node(block):
    lines = block.split("\n")
    if(not all(line.startswith(f"{i+1}. ") for i, line in enumerate(lines))):
        raise Exception("This is not a valid ordered list")
    children = []
    for line in lines:
        child = ParentNode("li", text_to_children(line[2:].strip()))
        children.append(child)
    return ParentNode("ol", children)

def code_to_html_node(block):
    lines = block.split("\n")
    if(not lines[-1].startswith("```") or not lines[-1].endswith("```")):
        raise Exception("This is not a valid code block")
    code = " ".join(block[3:-3].split("\n"))
    return ParentNode("pre", [ParentNode("code", text_to_children(code))])

def quote_to_html_node(block):
    lines = block.split("\n")
    if(not all(line.startswith("> ") for line in lines)):
        raise Exception("This is not a valid quote")
    content = " ".join([line.lstrip(">").strip() for line in lines])
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match(block_type):
        case "heading":
            return heading_to_html_node(block)
        case "paragraph":
            return paragraph_to_html_node(block)
        case "unordered_list":
            return unordered_list_to_html_node(block)
        case "ordered_list":
            return ordered_list_to_html_node(block)
        case "code":
            return code_to_html_node(block)
        case "quote":
            return quote_to_html_node(block)
        case _:
            raise ValueError("This is not a valid type of block")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)




def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path}")
    from_file = open(from_path, "r")
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    title = extract_title(markdown)
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_path_dir = os.path.dirname(dest_path)
    if(not os.path.exists(dest_path_dir)):
        os.makedirs(os.path.dirname(dest_path))

    write_file = open(dest_path, "w")
    write_file.write(template)
    write_file.close()

def generate_page_recursive(dir_path_content, template_path, dir_path_public):
    print(dir_path_content)
    for filename in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content, filename)
        if os.path.isfile(file_path):
            generate_page(file_path, template_path, os.path.join(dir_path_public, filename.replace("md", "html")))
        else:
            subdir_path = os.path.join(dir_path_public, filename)
            os.makedirs(subdir_path, exist_ok=True)
            generate_page_recursive(file_path, template_path, subdir_path)
