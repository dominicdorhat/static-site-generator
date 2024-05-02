import unittest
from textnode import TextNode
from texttype import TextType
from inline_markdown import split_nodes_delimiter

class TestInlineMarkdown(unittest.TestCase):

    def setUp(self):
        self.node = [TextNode("This is a word with a **bolded word** in it with **bold**", TextType.TEXT)]
        self.bolded_node = [TextNode("**bold**", TextType.TEXT)]

    def test_multiple_bolded_words_in_a_sentence(self):
        expected = [
                TextNode("This is a word with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" in it with ", TextType.TEXT),
                TextNode("bold", TextType.BOLD)
                ]
        print(split_nodes_delimiter(self.node, "**", TextType.BOLD))
        self.assertEqual(split_nodes_delimiter(self.node, "**", TextType.BOLD), expected)

    def test_one_bolded_word(self):
        expected = [TextNode("bold", TextType.BOLD)]
        self.assertEqual(split_nodes_delimiter(self.bolded_node, "**", TextType.BOLD), expected)
