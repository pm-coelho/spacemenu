import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject

from .branch import Branch
from .options import Options

# TODO: make private classes "private" (use _)
class Window:
    def __init__(self, root, options = None):
        self._options = Options(options)

        self._window = Gtk.Window(title=root['label'])
        self._screen = Gdk.Screen.get_default()
        self._display = self._screen.get_display()
        self._monitor = self._display.get_monitor_at_window(self._screen.get_root_window())

        # TODO: validate values for root
        self._root = Branch(root['label'], root['branches'], root['leaves'])
        self._init_signals()


    def _init_signals(self):
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

        self._window.connect('key-press-event', self._on_key_press)
        self._window.connect('branch', self._open_branch)
        self._window.connect('leaf', self._exec_leaf)
        self._window.connect('destroy', Gtk.main_quit)


    def _draw_contents(self, branch):
        self._current_branch = branch

        [self._window.remove(e) for e in self._window.get_children()]

        self._current_branch.gen_content(self._options)

        self._set_size(branch.n_rows)
        self._place()
        self._window.add(branch.content)
        self._window.show_all()


    def _set_size(self, n_rows):
        row_height = self._options.row_height
        row_spacing = self._options.row_spacing
        margin = self._options.margin

        self._width = self._monitor.get_geometry().width
        self._height = (margin * 2 ) + (n_rows * (row_height + row_spacing))

        self._window.resize(self._width, self._height)


    def _place(self):
        screen_height = self._screen.get_height()
        self._window.set_gravity(Gdk.Gravity.SOUTH_WEST)
        self._window.move(self._monitor.get_workarea().x, screen_height - self._height)


    def _on_key_press(self, window, event):
        key = Gdk.keyval_name(event.keyval)

        branch = self._current_branch.get_child_branch(key)
        if (branch):
            self._window.emit('branch', branch)
            return

        leaf = self._current_branch.get_child_leaf(key)
        if (leaf):
            self._window.emit('leaf', leaf)
            return


    def _open_branch(self, widget, branch):
        self._draw_contents(branch)


    def _exec_leaf(self, widget, leaf):
        leaf.exec()
        Gtk.main_quit()


    def draw(self):
        self._window.set_border_width(self._options.margin)
        self._draw_contents(self._root);
        Gtk.main()
