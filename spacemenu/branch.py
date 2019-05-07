import string
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from random import choice

from .node import Node
from .leaf import Leaf

# TODO: auto generate back button
# TODO: auto generate quit button


class Branch(Node):
    def __init__(self, name, branches, leaves, command):
        super(Branch, self).__init__(name, command, self)
        self._branches = [Branch(b['name'], b['branches'], b['leaves'], command) for b in branches]
        self._leaves = [Leaf(l['name'], l['command']) for l in leaves]
        self.gen_shortcuts()

    def gen_content(self, options):
        grid = Gtk.Grid()
        grid.set_column_spacing(options['column_spacing'])
        grid.set_row_spacing(options['row_spacing'])
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        buttons = [b.get_button() for b in self._branches + self._leaves if b.shortcut != None]

        row = 0
        for i, b in enumerate(buttons):
            row = int(i / (options['max_columns']))
            column = i % (options['max_columns'])
            grid.attach(b, column, row, 1, 1)

        self.content = grid
        self.n_rows = row + 1


    def gen_shortcuts(self):
        [b.set_shortcut(self.gen_shortcut(b.name)) for b in self._branches]
        [l.set_shortcut(self.gen_shortcut(l.name)) for l in self._leaves]


    def gen_shortcut(self, name):
        shortcut = None
        letters = name
        while (shortcut == None):
            if letters == '':
                letters = string.ascii_lowercase

            prop_shortcut = letters[0]
            if prop_shortcut not in string.ascii_lowercase:
                letters = letters[1:]

            used_shortcuts = self.get_used_shortcuts()
            if len(used_shortcuts) == len(string.ascii_letters):
                print('Shortcut limit reached! ignoring further shortcuts')
                return

            if (prop_shortcut not in used_shortcuts):
                shortcut = prop_shortcut
            elif (prop_shortcut.swapcase() not in used_shortcuts):
                shortcut = prop_shortcut.swapcase()
            else:
                letters = letters[1:]

        return shortcut


    def get_used_shortcuts(self):
        return [x.shortcut for x in self._leaves + self._branches if x.shortcut != None]
