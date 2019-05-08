import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject

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

        self._root = Branch(root['name'], root['branches'], root['leaves'])

        self.init_signals()


    def init_signals(self):
        GObject.signal_new(
            'branch',
            self._window,
            GObject.SignalFlags.RUN_FIRST,
            None,
            (GObject.TYPE_PYOBJECT,)
        )

        GObject.signal_new(
            'leaf',
            self._window,
            GObject.SignalFlags.RUN_FIRST,
            None,
            (GObject.TYPE_PYOBJECT,)
        )

        self._window.connect('key-press-event', self.on_key_press)
        self._window.connect('branch', self.open_branch)
        self._window.connect('leaf', self.exec_leaf)
        self._window.connect('destroy', Gtk.main_quit)


    def draw(self):
        self._window.set_border_width(self._options['margin'])
        self.draw_contents(self._root);
        Gtk.main()


    def draw_contents(self, branch):
        self.current_branch = branch

        for e in self._window.get_children():
            self._window.remove(e)

        branch.gen_content(self._options)

        self.set_size(branch.n_rows)
        self.place()
        self._window.add(branch.content)
        self._window.show_all()


    def set_size(self, n_rows):
        row_height = self._options['row_height']
        row_spacing = self._options['row_spacing']
        margin = self._options['margin']

        self._width = self._monitor.get_geometry().width
        self._height = (margin * 2 ) + (n_rows * (row_height + row_spacing))

        self._window.resize(self._width, self._height)


    def place(self):
        screen_height = self._screen.get_height()
        self._window.set_gravity(Gdk.Gravity.SOUTH_WEST)
        self._window.move(self._monitor.get_workarea().x, screen_height - self._height)


    def on_key_press(self, window, event):
        key = Gdk.keyval_name(event.keyval)

        branch = self.current_branch.get_child_branch(key)
        if (branch):
            self._window.emit('branch', branch)
            return

        leaf = self.current_branch.get_child_leaf(key)
        if (leaf):
            self._window.emit('leaf', leaf)
            return


    def open_branch(self, widget, branch):
        self.draw_contents(branch)
        pass


    def exec_leaf(self, widget, leaf):
        leaf.exec()
        Gtk.main_quit()
        pass
