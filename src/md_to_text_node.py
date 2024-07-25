from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if(text_type == "text"):
        return old_nodes
    for node in old_nodes:
        new_text = node.text.split(delimiter)
        if(len(new_text)%2 == 0):
            raise Exception("each opening delimiter must have a closing delimiter")
        is_normal_text = True 
        for text in new_text:
            new_nodes.append(TextNode(text, "text" if is_normal_text else text_type))
            is_normal_text = not is_normal_text
            print(new_nodes[-1])
    return new_nodes

