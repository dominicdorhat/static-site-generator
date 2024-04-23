class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        # used to indicate either:
        #   1. not implemented yet
        #   2. derived classes MUST override this method
        raise NotImplementedError()

   # return string representation of the HTML attributes of node
    def props_to_html(self):
        text = ""
        for key, value in self.props.items():
            text += f"{key}=\"{value}\" "

        # remove last space
        return text[:-1]

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
