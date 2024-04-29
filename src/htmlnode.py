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

    def props_to_html(self):
        props = ""
        if not self.props:
            return props
        else:
            for key, value in self.props.items():
                props += f" {key}=\"{value}\""

        # remove last space
        return props.rstrip()

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
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTML tag.")

        if not self.children:
            raise ValueError(f"{self.tag} has no valid children.")

        # base case: LeafNode
        # ex:  <body><p><b>Losum epsum</b></p></body>
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += f"{child.to_html()}"

        html += f"</{self.tag}>"
        return html

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
