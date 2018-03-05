import os
import magic


class Tree:
    def __init__(self, title, location, mime_type):
        """Creates a node of tree
        Args:
            self: Object of node of tree
            title: name of node
            location: path of node
        Returns:
            None
        """
        self.title = title
        self.location = location
        self.innodeNo = os.stat(location).st_ino
        self.modify = os.stat(location).st_mtime
        self.mimeType = mime_type

        try:
            children_list = os.listdir(location)
            self.childrenList = children_list
        except NotADirectoryError:
            self.childrenList = []
        self.children = []


def initialize_root():
    """
    initializes the root of tree
    :return: instance of root
    """
    title = 'Google Drive'
    with open('/usr/local/apps/cloud drive/HOME', 'r') as home:
        home_dir = home.read()
        home.close()
    location = home_dir + '/Google Drive'
    root = Tree(title=title, location=location, mime_type='inode/directory')
    return root


def build_tree(children_list, current_location, current_node):
    """
    Uses preorder traversing to get structure of tree

    :param current_location: defines the url of folder on which traversing is being done
    :param children_list: lists of files or folders which comes under currentRoot
    :param current_node: object of current node
    :return: None
    """

    for title in children_list:

        children_location = current_location + "/" + title

        if magic.Magic(flags=magic.MAGIC_MIME_TYPE).id_filename(children_location) == 'inode/directory':

            node = Tree(title=title, location=children_location, mime_type='inode/directory')
            current_node.children.append(node)
            build_tree(node.childrenList, node.location, node)
        else:
            node = Tree(title=title, location=children_location, mime_type='file')
            current_node.children.append(node)


def get_tree():
    """
    get the root of tree of Google Drive folder
    :return: instance of root of tree
    """
    root = initialize_root()
    build_tree(children_list=root.childrenList, current_location=root.location, current_node=root)
    return root


def traverse(node):
    """
    traverses a tree of given node
    :param node: instance of node needed to be traversed
    :return: None
    """
    if node:
        print(node, node.title, node.innodeNo, node.modify, node.location, node.childrenList, node.children, '\n')
        for i in node.children:
            traverse(i)
    return None


def create_node(title, location, mime_type):
    """
    creates a new node
    :param title: name field of node
    :param location: location of file
    :param mime_type: mimetype of file
    :return: node instance
    """
    node = Tree(title=title, location=location, mime_type=mime_type)
    return node


def append_child(parent, new_child):
    """
    appends a node as child to a parent node
    :param parent: parent node
    :param new_child: node to be added as child
    :return: None
    """
    parent.children.append(new_child)
    parent.childrenList.append(new_child.title)
    return None


def save_tree(root, file):
    """
    Builds a json tree of desktop tree and save into a location
    :param root: root of the desktop tree in memory
    :param file: location of file where tree needs to e saved
    :return: None
    """
    d = dictionary_desktop_tree(root=root)
    import json
    with open(file, 'w') as jsonfile:
        data = json.dumps(d)
        jsonfile.write(data)
    return None


def dictionary_desktop_tree(root):
    d = {
        'title': root.title,
        'innodeNo': root.innodeNo,
        'modify': root.modify,
        'mimeType': '',
        'children': []
    }
    if root.mimeType == 'inode/directory':
        d['mimeType'] = 'inode/directory'
        for child in root.children:
            d['children'].append(dictionary_desktop_tree(root=child))
    else:
        d['mimeType'] = 'file'

    return d
