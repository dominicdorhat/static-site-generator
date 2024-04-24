from htmlnode import HTMLNode

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

    # TODO:
    def __repr__(self):
        pass
