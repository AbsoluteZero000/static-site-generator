from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
       super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if(self.value is None):
            raise ValueError("All leaf Nodes must have a value")
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>" if self.tag is not None else self.value 

