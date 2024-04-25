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
        if not self.props:
            return text
        else:
            for key, value in self.props.items():
                text += f" {key}=\"{value}\""

        # remove last space
        # return text[:-1]
        return text.rstrip()

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode has no value")

        html_string = ""
        if not self.tag:
            return self.value

        # space_prefix = " "
        html_string += f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return html_string

    def __repr__(self):
        return f"LeafNode({self.tag},{self.value},{self.props})"
