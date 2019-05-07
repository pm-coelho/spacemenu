import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from .branch import Branch

class Window:
    def __init__(self, root, options):
        # TODO: set default options
        # TODO: externally validate values for options
        self._options = options

        self._window = Gtk.Window(title=root['name'])
        self._screen = Gdk.Screen.get_default()
        self._display = self._screen.get_display()
        self._monitor = self._display.get_monitor_at_window(self._screen.get_root_window())

        self._root = Branch(root['name'], root['branches'], root['leaves'], self.redraw)

        self.on_kill()


    def draw(self):
        self.current_branch = self._root

        self._window.set_border_width(self._options['margin'])
        self.set_styles()

        self._root.gen_content(self._options)

        self._window.connect('key-press-event', self.on_key_press)

        self.set_size(self._root.n_rows)
        self.place()
        self._window.add(self._root.content)
        self._window.show_all()
        Gtk.main()


    def redraw(self, button, branch):
        for e in self._window.get_children():
            self._window.remove(e)

        self.current_branch = branch
        branch.gen_content(self._options)

        self.set_size(branch.n_rows)
        self.place()
        self._window.add(branch.content)
        self._window.show_all()

    def on_key_press(self, window, event):
        print('widget: ', window)
        print('modifier: ', event.state)
        print('key val, name: ', event.keyval, Gdk.keyval_name(event.keyval))
        pass

    def set_styles(self):
        pass


    def set_size(self, n_rows):
        row_height = self._options['row_height']
        row_spacing = self._options['row_spacing']
        margin = self._options['margin']

        self._width = self._monitor.get_geometry().width
        self._height = (margin * 2 ) + (n_rows * (row_height + row_spacing))

        self._window.set_default_size(self._width, self._height)


    def place(self):
        screen_height = self._screen.get_height()
        self._window.set_gravity(Gdk.Gravity.SOUTH_WEST)
        self._window.move(0, screen_height - self._height)


    def on_kill(self):
        self._window.connect('destroy', Gtk.main_quit)
