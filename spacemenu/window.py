import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from .branch import Branch

class Window:
    def __init__(self, root, options):
        self._window = Gtk.Window(title=root['name'])
        self._screen = Gdk.Screen.get_default()
        self._root = Branch(root['name'], root['branches'], root['leaves'])
        self.on_kill()
        # TODO: set default options
        self._options = options

    def draw(self, branch = None):
        if (branch == None):
            branch = self._root
        self.current_branch = branch
        self._window.set_border_width(self._options['margin'])
        self.set_styles()

        (n_rows, content) = branch.get_content(self._options)
        self.set_size(n_rows)
        self.place()

        self._window.add(content)
        self._window.show_all()
        Gtk.main()

    def set_styles(self):
        pass

    def set_size(self, n_rows):
        #TODO: externally validate values for options
        row_height = self._options['row_height']
        row_spacing = self._options['row_spacing']
        margin = self._options['margin']

        self._width = self._screen.get_width()
        self._height = (margin * 2 ) + (n_rows * (row_height + row_spacing))

        self._window.set_default_size(self._width, self._height)


    def place(self):
        screen_height = self._screen.get_height()
        self._window.set_gravity(Gdk.Gravity.SOUTH_WEST)
        self._window.move(0, screen_height - self._height)

    def on_kill(self):
        self._window.connect('destroy', Gtk.main_quit)
