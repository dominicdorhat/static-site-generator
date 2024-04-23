import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    nodeh1 = HTMLNode("h1", "README")
    nodeLink = HTMLNode("a", "This is a link", props = {"href": "https://www.boot.dev"})
    nodeLink2 = HTMLNode("a", "This is a 2nd link", props = {"href": "https://www.boot.dev", "target": "_blank"})
    nodeEmptyP = HTMLNode("p")
    nodeRawText = HTMLNode(value="Raw Text")
    nodeEmptyNode = HTMLNode()

    node_children = [nodeh1, nodeLink, nodeEmptyP]

    nodeHTML = HTMLNode("html",children = node_children)

#    def test_htmlException(self):
#       self.assertIs(self.nodeh1.to_html(), NotImplementedError())

    def test_props_to_html(self):
        self.assertEqual(self.nodeLink.props_to_html(), "href=\"https://www.boot.dev\"")
        self.assertEqual(self.nodeLink2.props_to_html(), "href=\"https://www.boot.dev\" target=\"_blank\"")

    def test_none(self):
        self.assertIsNone(self.nodeEmptyNode.tag)
        self.assertIsNone(self.nodeEmptyNode.value)
        self.assertIsNone(self.nodeEmptyNode.children)
        self.assertIsNone(self.nodeEmptyNode.props)

    def test_RawText(self):
        self.assertEqual(self.nodeRawText.value, "Raw Text")
        self.assertIsNone(self.nodeRawText.tag)
        self.assertIsNone(self.nodeRawText.children)
        self.assertIsNone(self.nodeRawText.props)

    if __name__ == "__main__":
        unittest.main()
