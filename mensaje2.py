import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class MensajeInicio(Gtk.MessageDialog):
    """Clase MessageDialog"""
    def __init__(self, parent):
        super().__init__(title="Realizando simulación",
                        transient_for=parent)
        self.set_markup("Espere un momento por favor...")
