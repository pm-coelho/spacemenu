from .node import Node
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

import os

class Leaf(Node):
    def __init__(self, name, command):
        super(Leaf, self).__init__(name)
        self.command = command


    def exec(self):
        Gtk.main_quit()
        #TODO: this is a security vuln:https://docs.python.org/2/library/subprocess.html#frequently-used-arguments
        os.system(self.command)
