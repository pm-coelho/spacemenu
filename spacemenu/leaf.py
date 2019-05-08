from .node import Node

import os

class Leaf(Node):
    def __init__(self, name, command):
        super(Leaf, self).__init__(name)
        self._command = command


    def exec(self):
        #TODO: this is a security vuln:https://docs.python.org/2/library/subprocess.html#frequently-used-arguments
        os.system(self._command)
