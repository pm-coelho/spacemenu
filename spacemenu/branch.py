import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from random import choice

from .node import Node
from .leaf import Leaf

class Branch(Node):
    def __init__(self, name, branches, leaves):
        super(Branch, self).__init__(name)
        self._branches = [Branch(b['name'], b['branches'], b['leaves']) for b in branches]
        self._leaves = [Leaf(l['name']) for l in leaves]
        self.gen_shortcuts()


    def get_content(self, options):
        grid = Gtk.Grid()
        grid.set_column_spacing(options['column_spacing'])
        grid.set_row_spacing(options['row_spacing'])
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        buttons = [b.get_button() for b in self._branches + self._leaves]

        for i, b in enumerate(buttons):
            row = int(i / (options['max_columns']))
            column = i % (options['max_columns'])
            grid.attach(b, column, row, 1, 1)

        return (row + 1 , grid)


    def gen_shortcuts(self):
        [b.set_shortcut(self.gen_shortcut(b.name)) for b in self._branches]
        [l.set_shortcut(self.gen_shortcut(l.name)) for l in self._leaves]


    def gen_shortcut(self, name):
        # TODO: this turns into an infinite loop when no more letters are available
        # TODO: define available shortcuts (don't use string.letters)
        # TODO: this will use unallowed keys as shortcut (ex. space)
        if name == '': return self.gen_shortcut(choice(string.letters))

        shortcut = name[0]
        used_shortcuts = self.get_used_shortcuts()
        if (shortcut not in used_shortcuts):
            return shortcut
        elif (shortcut.swapcase() not in used_shortcuts):
            return shortcut.swapcase()
        else:
            return self.gen_shortcut(name[1:])


    def get_used_shortcuts(self):
        return [x.shortcut for x in self._leaves + self._branches]
