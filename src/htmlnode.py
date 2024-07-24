import functools
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag if tag is not None else "p"
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return " ".join([f"{key}=\"{value}\""for key, value in self.props.items()])

    def __repr__(self):
        return f"tag = {self.tag}\nvalue = {self.value}\nchildren = {self.children}\nprops = {self.props}"
