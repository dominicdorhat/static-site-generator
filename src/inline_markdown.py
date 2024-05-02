from texttype import TextType
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # old_nodes = list of TextNodes
    # TODO: check for pairing delimiter

    new_nodes = []
    # n^2 operation...
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.extend(node)

        # TODO: split by word or delimiter
        new_nodes.extend(text_to_node(node.text.split(), delimiter))

    return new_nodes

def text_to_node(text_list, delimiter):
    new_list = []
    text =  ""
    delimited_word = ""
    delimiter_exist = False

    for word in text_list:
        if word[0] == delimiter and len(word) > 1 and not delimiter_exist:
            delimited_word += word.strip(delimiter)
            delimiter_exist = True

            if text:
                new_list.extend(TextNode(text, TextType.TEXT))
                text = ""

            if word[-1] == delimiter:
                new_list.extend(TextNode(word.strip(delimiter), delimiter_converter(delimiter)))
                delimiter_exist = False

        elif word[-1] == delimiter and len(word > 1 and delimiter_exist:
            new_list.extend(TextNode(delimited_word + ' ' + word.strip(delimiter), delimiter_converter(delimiter)))
            delimited_word = ""

        elif word[-1] == delimiter and not delimiter_exist:
            raise Exception("Invalid delimiter used")

        else:
            text += word + ' '


def delimiter_converter(delimiter):
    match delimiter:
        case '**':
            return TextType.BOLD
        case '*':
            return TextType.ITALIC
        case '`':
            return TextType.CODE
        # TODO: link

        # TODO: determine if necessary
        case _:
            return Exception("Invalid delimiter type")
