from .node import Node

class Leaf(Node):
    def __init__(self, name):
        super(Leaf, self).__init__(name)
