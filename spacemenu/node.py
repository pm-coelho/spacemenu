import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class _Node:
    def __init__(self, label, style_provider):
        self._style_provider = style_provider
        self.label = label
        self.shortcut = None


    def _on_click(self, button, args):
        button_type = self.__class__.__name__.lower()
        window = button.get_parent().get_parent()
        window.emit(button_type[1:], self)


    def set_shortcut(self, shortcut):
        self.shortcut = shortcut


    def get_button(self, options):
        button = Gtk.Button("")

        shortcut_color = None
        separator_color = None
        label_color = None

        if (type(self).__name__ == '_Branch'):
            style_context = button.get_style_context()
            style_context.add_class('branch_button')
            shortcut_color = options.branch_text_shortcut_color
            separator_color = options.branch_text_separator_color
            label_color = options.branch_text_label_color
        elif (type(self).__name__ == '_Leaf'):
            style_context = button.get_style_context()
            style_context.add_class('leaf_button')
            shortcut_color = options.leaf_text_shortcut_color
            separator_color = options.leaf_text_separator_color
            label_color = options.leaf_text_label_color

        shortcut = '<span color="#{color}">{shortcut:1}</span>'.format(
            color = shortcut_color,
            shortcut = self.shortcut
        ) if (shortcut_color != None) else '{shortcut:1}'.format(shortcut = self.shortcut)

        separator = '<span color="#{color}">{separator:2}</span>'.format(
            color = separator_color,
            separator = '->'
        ) if (separator_color != None) else '{separator:2}'.format(separator = '->')

        label = '<span color="#{color}">{label:10}</span>'.format(
            color = label_color,
            label = self.label
        ) if (label_color != None) else '{label:10}'.format(label = self.label)

        for child in button.get_children():
            child.set_label('<b>{}</b> {} {}'.format(shortcut, separator, label))
            child.set_use_markup(True)


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

