import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    # [Test Nodes]
    nodeh1 = HTMLNode("h1", "README")
    nodeLink = HTMLNode("a", "This is a link", props = {"href": "https://www.boot.dev"})
    nodeLink2 = HTMLNode("a", "This is a 2nd link", props = {"href": "https://www.boot.dev", "target": "_blank"})
    nodeEmptyP = HTMLNode("p")
    nodeRawText = HTMLNode(value="Raw Text")
    nodeEmptyNode = HTMLNode()

    node_children = [nodeh1, nodeLink, nodeEmptyP]

    nodeHTML = HTMLNode("html",children = node_children)

    ## [LeafNodes]
    nodeRawTextLN = LeafNode(None, "Raw Text")
    nodeh1LN = LeafNode("h1", "README")
    nodeLinkLN = LeafNode("a", "Click me!", props={"href": "www.boot.dev"})
    nodeLink2LN = LeafNode("a", "Click me too!", props={"href": "www.boot.dev", "target": "_blank"})

#   How to test for Exceptions? Unless you don't.
#    def test_htmlException(self):
#       self.assertIs(self.nodeh1.to_html(), NotImplementedError())

    def test_props_to_html(self):
        self.assertEqual(self.nodeLink.props_to_html(), " href=\"https://www.boot.dev\"")
        self.assertEqual(self.nodeLink2.props_to_html(), " href=\"https://www.boot.dev\" target=\"_blank\"")

    def test_none(self):
        self.assertIsNone(self.nodeEmptyNode.tag)
        self.assertIsNone(self.nodeEmptyNode.value)
        self.assertIsNone(self.nodeEmptyNode.children)
        self.assertIsNone(self.nodeEmptyNode.props)

    def test_raw_textHTML(self):
        self.assertEqual(self.nodeRawText.value, "Raw Text")
        self.assertIsNone(self.nodeRawText.tag)
        self.assertIsNone(self.nodeRawText.children)
        self.assertIsNone(self.nodeRawText.props)

    def test_raw_textLN(self):
        self.assertEqual(self.nodeRawTextLN.to_html(), "Raw Text")

    def test_h1LN(self):
        self.assertEqual(self.nodeh1LN.to_html(), "<h1>README</h1>")

    def test_link_props_to_html(self):
        self.assertEqual(self.nodeLinkLN.to_html(), "<a href=\"www.boot.dev\">Click me!</a>")
        self.assertEqual(self.nodeLink2LN.to_html(), "<a href=\"www.boot.dev\" target=\"_blank\">Click me too!</a>")


    if __name__ == "__main__":
        unittest.main()
