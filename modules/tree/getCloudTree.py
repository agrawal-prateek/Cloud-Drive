import json

mime_type = None
modified_date = None
title = None


def build_tree(items_list, item_id, parent, drive_service):
    global title, mime_type, modified_date
    for k in items_list:

        if k['id'] == item_id:
            labels = k['labels']
            if labels['hidden'] or labels['trashed']:
                return None
            title = k['title']
            mime_type = k['mimeType']
            modified_date = k['modifiedDate']
            break
    item = Tree(nodeid=item_id, node_title=title, mimetype=mime_type, node_modified_date=modified_date)
    item.add_parent(parent)
    parent.add_child(item)

    item_children = drive_service.children().list(folderId=item_id).execute()
    item_children = item_children['items']
    for k in item_children:
        build_tree(items_list=items_list, item_id=k['id'], parent=item, drive_service=drive_service)


def build_root(drive_service):
    root_details = drive_service.files().get(fileId="root").execute()
    root_instance = Tree(nodeid=root_details['id'], node_title='My Drive', mimetype=root_details['mimeType'],
                         node_modified_date=root_details['modifiedDate'])
    return root_instance


class Tree:
    def __init__(self, nodeid, node_title, mimetype, node_modified_date):
        """
        Initializes the attributes of instance of tree
        :param nodeid: id of item on cloud
        :param node_title: title of item on cloud
        :param mimetype: mimetype of item
        :param node_modified_date: latest moification date on cloud
        """
        self.id = nodeid
        self.title = node_title
        self.mimeType = mimetype
        self.modifiedDate = node_modified_date
        self.parent = []
        self.children = []

    def add_child(self, child_object):
        self.children.append(child_object)

    def add_parent(self, parent_object):
        self.parent.append(parent_object)


def get_tree(drive_service):
    """
    Builds a tree data structure for items on cloud
    :param drive_service: servive object for drive
    :return: instance of root of the tree if tree builded successfully else False
    """

    files = drive_service.files().list().execute()
    if not files['incompleteSearch']:
        files = files['items']
        root = build_root(drive_service=drive_service)
        root_children = drive_service.children().list(folderId=root.id).execute()
        root_children = root_children['items']
        for i in root_children:
            build_tree(items_list=files, item_id=i['id'], parent=root, drive_service=drive_service)
        return root
    else:
        print('incomplete search')
        return False


def traverse(node):
    print(node.parent, node.id, node.title, node.mimeType, node.modifiedDate, node.children)
    for child in node.children:
        traverse(child)


def save_items_list(drive_service, file_location):
    """
    save cloud items list in a json file
    :param file_location: location where file needs to be saved
    :param drive_service: servive object for drive
    :return: True if list successfully saved else false
    """
    files = drive_service.files().list().execute()
    if not files['incompleteSearch']:
        files = files['items']
        dict_to_json_dump = json.dumps(files)

        with open(file_location, 'w+') as json_file:
            json_file.write(dict_to_json_dump)
            json_file.close()
        return True
    return False


def save_tree(root, file_location):
    """
    Builds a json tree of desktop tree and save into a location
    :param root: root of the desktop tree in memory
    :param file_location: location of file where tree needs to e saved
    :return: None
    """
    d = dict()

    d['id'] = root.id
    d['title'] = root.title
    d['mimeType'] = root.mimeType
    d['modifiedDate'] = root.modifiedDate
    d['parent'] = root.parent
    d['children'] = []

    for child in root.children:
        d['children'].append(dictionary_cloud_tree(root=child))
    print(d)
    with open(file_location, 'w') as jsonfile:
        data = json.dumps(d)
        jsonfile.write(data)
    return None


def dictionary_cloud_tree(root):
    if root.mimeType == 'application/vnd.google-apps.folder':
        d = {
            'id': root.id,
            'title': root.title,
            'mimeType': 'application/vnd.google-apps.folder',
            'modifiedDate': root.modifiedDate,
            'parent': root.parent[0].id,
            'children': []
        }
    else:
        d = {
            'id': root.id,
            'title': root.title,
            'mimeType': root.mimeType,
            'modifiedDate': root.modifiedDate,
            'parent': root.parent[0].id,
            'children': []
        }
    for child in root.children:
        d['children'].append(dictionary_cloud_tree(root=child))
    return d
