import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class _Node:
    def __init__(self, label, style_provider):
        self._style_provider = style_provider
        self.label = label
        self.shortcut = None

    def _on_click(self, button, args):
        type = self.__class__.__name__.lower()
        window = button.get_parent().get_parent()
        window.emit(type, self)

    def set_shortcut(self, shortcut):
        self.shortcut = shortcut


    def get_button(self):
        button = Gtk.Button.new_with_label('{shortcut:1}{separator:2}{label:10}'.format(
            shortcut = self.shortcut,
            separator = '->',
            label= self.label
        ))

        button.connect('clicked', self._on_click, None)

        button.get_style_context().add_provider(
            self._style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        for c in button.get_children():
            c.set_justify(Gtk.Justification.LEFT)
            c.set_halign(Gtk.Align.START)
            c.set_use_markup(True)

        return button

