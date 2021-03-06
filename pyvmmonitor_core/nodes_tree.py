# License: LGPL
#
# Copyright: Brainwy Software

import sys


class Node(object):

    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, node):
        assert isinstance(node, Node)
        self.children.append(node)
        return node

    def __hash__(self, *args, **kwargs):
        raise AssertionError('unhashable')

    def __len__(self):
        count = len(self.children)
        for c in self.children:
            count += len(c)
        return count


class NodesTree(Node):  # Special node with no associated data

    def __init__(self):
        Node.__init__(self, None)

    def print_rep(self, node=None, level=0, stream=None):
        if stream is None:
            stream = sys.stderr

        if node is None:
            node = self

        pre = ' ' * (2 * level)
        for child in node.children:
            stream.write(u'%s%s: %s\n' % (pre, child.data.__class__.__name__, child.data))
            self.print_rep(child, level + 1, stream)

    def as_str(self):
        from io import StringIO
        s = StringIO()
        self.print_rep(stream=s)
        return s.getvalue()
