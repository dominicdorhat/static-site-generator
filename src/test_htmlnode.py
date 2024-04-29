import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    # [Test Nodes]
    nodeh1 = HTMLNode("h1", "README")
    nodeLink = HTMLNode("a", "This is a link", props = {"href": "https://www.boot.dev"})
    nodeLink2 = HTMLNode("a", "This is a 2nd link", props = {"href": "https://www.boot.dev", "target": "_blank"})
    nodeRawText = LeafNode(None, value="Raw Text")
    nodeEmptyNode = HTMLNode()

    ## [LeafNodes]
    nodeh1LN = LeafNode("h1", "README")
    nodeLinkLN = LeafNode("a", "Click me!", props={"href": "www.boot.dev"})
    nodeLink2LN = LeafNode("a", "Click me too!", props={"href": "www.boot.dev", "target": "_blank"})
    nodeRawTextLN = LeafNode(None, "Raw Text")

    ## [Parent Nodes]
    nodeP = ParentNode("p", [LeafNode("b", "Lorem epsum")])
    nodeBody = ParentNode("body", children = [nodeh1LN, nodeP])

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

    def test_link_to_html(self):
        self.assertEqual(self.nodeLinkLN.to_html(), "<a href=\"www.boot.dev\">Click me!</a>")
        self.assertEqual(self.nodeLink2LN.to_html(), "<a href=\"www.boot.dev\" target=\"_blank\">Click me too!</a>")

    def test_render_to_html(self):
        node = LeafNode("a", "link")
        self.assertEqual(self.nodeBody.to_html(), "<body><h1>README</h1><p><b>Lorem epsum</b></p></body>")

    def test_nested_parents_to_html(self):
        nodeLink = LeafNode("a", "Click me too!", props={"href": "www.boot.dev", "target": "_blank"})
        node = ParentNode("html", [
                ParentNode("head", [LeafNode("h1", "HEADER"), nodeLink]),
                ParentNode("body", [ParentNode("p", [LeafNode("i", "Lorem Ipsum"), LeafNode(None, "raw text")])])])

        self.assertEqual(node.to_html(), "<html><head><h1>HEADER</h1><a href=\"www.boot.dev\" target=\"_blank\">Click me too!</a></head><body><p><i>Lorem Ipsum</i>raw text</p></body></html>")

    def test_linear_to_html(self):
        # multiple levels deep but 1 child per level

        node = ParentNode("html", [ParentNode("body", [ParentNode("p", [ParentNode("b", [LeafNode("i", "Hello")])])])])
        print(node)

        self.assertEqual(node.to_html(), "<html><body><p><b><i>Hello</i></b></p></body></html>")

    if __name__ == "__main__":
        unittest.main()
