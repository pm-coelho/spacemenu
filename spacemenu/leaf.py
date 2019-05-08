from .node import _Node

import os

class _Leaf(_Node):
    def __init__(self, label, command):
        super(_Leaf, self).__init__(label)
        self._command = command


    def exec(self):
        #TODO: this is a security vuln:https://docs.python.org/2/library/subprocess.html#frequently-used-arguments
        os.system(self._command)
