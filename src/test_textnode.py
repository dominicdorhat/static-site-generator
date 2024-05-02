import unittest

from textnode import TextNode, text_node_to_html_node
# from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("node", "bold")
        self.assertNotEqual(node, node2)

    def test_urlNone(self):
        node = TextNode("This is a text node", "bold")
        self.assertIsNone(node.url)

    def test_texttype_noteq(self):
        node = TextNode("This is a text node", "italics")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node.text_type, node2.text_type)

    # def test_invalid_texttype_conversion(self):
    #     node = TextNode("", "strikethrough")
    #     self.assertRaises(Exception, text_node_to_html_node(node), msg="Invalid text type")

    # def test_imagetype_conversion(self):
    #     node = TextNode("image of a horse", "image", "horse.png")
    #     self.assertEqual(text_node_to_html_node(node), LeafNode("img", "", props={"src": "horse.png", "alt": "image of a horse"}))

    # TODO: equality cant be tested without LeafNode without overriding __eq__!
    # def test_rawtype_conversion(self):
    #     node = TextNode("raw text", "text")
    #     leaf_node = LeafNode(None, "raw text", None)
    #     converted_node = text_node_to_html_node(node)
    #     self.assertEqual(converted_node, LeafNode(None, "raw text"))

    if __name__ == "__main__":
        unittest.main()
