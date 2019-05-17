import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject

from .branch import _Branch
from .options import Options

# TODO: allow externally defined shortcuts

class Window:
    def __init__(self, root, options = None):
        self._options = options if isinstance(options, Options) else Options(options)

        self._window = Gtk.Window(title=root['label'])
        self._screen = Gdk.Screen.get_default()
        self._display = self._screen.get_display()
        self._monitor = self._display.get_monitor_at_window(self._screen.get_root_window())

        self._set_style(self._options)

        self._root = _Branch(root['label'], root['branches'], root['leaves'], self._style_provider)
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
        self._previous_branch = self._current_branch if hasattr(self,'_current_branch') else None
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
        inner_margin = self._options.inner_margin

        self._width = self._monitor.get_geometry().width
        self._height = (inner_margin * 2 ) + (n_rows * (row_height + row_spacing))

        if (self._options.margin_left): self._width -= self._options.margin_left
        if (self._options.margin_right): self._width -= self._options.margin_right

        self._window.resize(self._width, self._height)


    # TODO: this will need thought for multiple screens
    def _place(self):
        screen_height = self._screen.get_height()
        self._window.set_gravity(Gdk.Gravity.SOUTH_WEST)
        (x, _)= self._window.get_position()

        if (self._options.margin_left): x += self._options.margin_left

        y = screen_height - self._height
        if (self._options.margin_bottom):
            y -= self._options.margin_bottom


        self._window.move(x, y)


    def _on_key_press(self, window, event):
        key = Gdk.keyval_name(event.keyval)

        if (key == 'q' or key == 'Escape'):
            Gtk.main_quit()
            return

        if (key == 'b'):
            if (self._previous_branch):
                self._window.emit('branch', self._previous_branch)
            else:
                Gtk.main_quit()

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


    def _set_style(self, options):
        self._window.set_border_width(self._options.inner_margin)
        self._style_provider = Gtk.CssProvider()
        self._style_provider.load_from_data(self._construct_css(options))
        self._window.get_style_context().add_provider(
            self._style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )


    def _construct_css(self, options):
        styles = 'window {'
        if (options.background_color):
            styles += 'background-color: #{}; '.format(options.background_color)

        if (options.inner_margin):
            styles += 'margin: {}px; '.format(options.inner_margin)
        styles += '} '

        styles += 'button {'
        if (options.button_background_color):
            styles += 'background-color: #{};'.format(options.button_background_color)

        if (options.button_text_color):
            styles += 'color: #{};'.format(options.button_text_color)

        if (options.font):
            styles += 'font: {};'.format(options.font)
        styles += '} '

        return bytes(styles.encode())


    def draw(self):
        self._draw_contents(self._root);
        Gtk.main()
