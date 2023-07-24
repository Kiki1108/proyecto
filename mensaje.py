import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class Mensaje(Gtk.MessageDialog):
    """Clase MessageDialog"""
    def __init__(self, parent, title, texto, button):
        super().__init__(title=title,
                        transient_for=parent)
        self.set_markup(texto)
        if button:
            self.add_button("_Cerrar", Gtk.ResponseType.OK)