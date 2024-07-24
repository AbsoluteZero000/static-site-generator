from htmlnode import HTMLNode
from functools import reduce
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)
        print(self.children)
    
        
    def to_html(self):
        print(self.children)
        if(self.tag is None):
            raise ValueError("tag doesn't have a value")
        if(self.children is None or len(self.children) == 0):
            raise ValueError("children can't be empty")
        return f"<{self.tag}{self.props_to_html()}>" + reduce(lambda string_so_far, b: string_so_far + b.to_html(), self.children, "") + f"</{self.tag}>"
