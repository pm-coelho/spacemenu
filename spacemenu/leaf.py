from .node import _Node

import os

class _Leaf(_Node):
    def __init__(self, label, command, style_provider):
        super(_Leaf, self).__init__(label, style_provider)
        self._command = command


    def exec(self):
        #TODO: this is a security vuln:https://docs.python.org/2/library/subprocess.html#frequently-used-arguments
        os.system(self._command)
