import functools
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if(self.props is None):
            return ""
        if(len(self.props) == 0):
            return ""
        return " " + " ".join([f"{key}=\"{value}\""for key, value in self.props.items()])

    def __repr__(self):
        return f"tag = {self.tag}\nvalue = {self.value}" + ("" if(self.children is None) else (f"\nchildren = {self.children}")) + f"\nprops = {self.props}"
