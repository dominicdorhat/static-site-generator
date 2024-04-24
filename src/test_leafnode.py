import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    nodeRawText = LeafNode(None, "Raw Text")
    nodeh1 = LeafNode("h1", "README")
    nodeLink = LeafNode("a", "Click me!", props={"href": "www.boot.dev"})
    nodeLink2 = LeafNode("a", "Click me too!", props={"href": "www.boot.dev", "target": "_blank"})

    def test_raw_text(self):
        self.assertEqual(self.nodeRawText.to_html(), "Raw Text")

    def test_h1(self):
        self.assertEqual(self.nodeh1.to_html(), "<h1>README</h1>")

    def test_link_props_to_html(self):
        self.assertEqual(self.nodeLink.to_html(), "<a href=\"www.boot.dev\">Click me!</a>")
        self.assertEqual(self.nodeLink2.to_html(), "<a href=\"www.boot.dev\" target=\"_blank\">Click me too!</a>")


    if __name__ == "__main__":
        unittest.main()
