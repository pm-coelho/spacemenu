import string
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from random import choice

from .node import _Node
from .leaf import _Leaf


class _Branch(_Node):
    def __init__(self, label, branches, leaves, style_provider):
        super(_Branch, self).__init__(label, style_provider)
        self._branches = sorted(
            [_Branch(b['label'], b['branches'], b['leaves'], style_provider) for b in branches],
            key = lambda b: b.label
        )
        self._leaves = sorted(
            [_Leaf(l['label'], l['command'], style_provider) for l in leaves],
            key = lambda l: l.label
        )
        self._gen_shortcuts()


    def _gen_shortcuts(self):
        [b.set_shortcut(self._get_shortcut(b.label)) for b in self._branches]
        [l.set_shortcut(self._get_shortcut(l.label)) for l in self._leaves]


    def _get_shortcut(self, label):
        shortcut = None
        letters = label
        while (shortcut == None):
            if letters == '':
                letters = string.ascii_lowercase

            prop_shortcut = letters[0]
            if prop_shortcut not in string.ascii_lowercase:
                letters = letters[1:]

            used_shortcuts = self._get_used_shortcuts()
            if len(used_shortcuts) == len(string.ascii_letters):
                print('Shortcut limit reached! ignoring further shortcuts')
                return

            if (prop_shortcut not in string.ascii_letters):
                letters = letters[1:]
            elif (prop_shortcut not in used_shortcuts):
                shortcut = prop_shortcut
            elif (prop_shortcut.swapcase() not in used_shortcuts):
                shortcut = prop_shortcut.swapcase()
            else:
                letters = letters[1:]

        return shortcut


    def _get_used_shortcuts(self):
        return [x.shortcut for x in self._leaves + self._branches if x.shortcut != None] + ['b','q']


    def get_child_branch(self, shortcut):
        return next((b for b in self._branches if b.shortcut == shortcut), None)


    def get_child_leaf(self, shortcut):
        return next((l for l in self._leaves if l.shortcut == shortcut), None)


    def gen_content(self, options):
        grid = Gtk.Grid()
        grid.set_column_spacing(options.column_spacing)
        grid.set_row_spacing(options.row_spacing)
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        buttons = [b.get_button() for b in self._branches + self._leaves if b.shortcut != None]

        row = 0
        for i, b in enumerate(buttons):
            row = int(i / (options.max_columns))
            column = i % (options.max_columns)
            grid.attach(b, column, row, 1, 1)

        self.content = grid
        self.n_rows = row + 1
