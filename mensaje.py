import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class MensajeError(Gtk.MessageDialog):
    """Clase MessageDialog"""
    def __init__(self, parent, texto):
        super().__init__(title="Error",
                        transient_for=parent)
        self.set_markup(texto)
        self.add_button("_Cerrar", Gtk.ResponseType.OK)