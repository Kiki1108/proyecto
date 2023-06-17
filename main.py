import sys
import gi

gi.require_version('Gtk', '4.0')

from gi.repository import Gio, GObject, Gtk, Gdk, GdkPixbuf, GLib
from time import sleep
from simulacion import Simulacion
from enfermedad import Enfermedad
from comunidad import Comunidad


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = self.get_application()
        # Crear Header Bar
        header_bar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=header_bar)
        self.set_title("Simulación")
        # Crear el menu button
        menu_button_model = Gio.Menu()
        menu_button_model.append("About", "app.about")
        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=menu_button_model)
        header_bar.pack_end(child=menu_button)
        # Botón para empezar la simualción
        self.start_button = Gtk.Button.new_with_label("Empezar simulación")
        self.start_button.connect("clicked",self.on_start_button_clicked)
        # Crear la ventana
        self.main_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 10)
        self.set_child(self.main_box)
        self.main_box.append(self.start_button)


    def on_start_button_clicked(self, button):
        """
        Valores bases para la clase Enfermedad, Comunidad y Simulacion
        """
        infeccion_probable = 5
        infeccion_estrecho = 70
        promedio_pasos = 10
        mortalidad = 2
        enfermedad = Enfermedad(infeccion_probable, infeccion_estrecho,
                                promedio_pasos, mortalidad)
        """
        Valores bases para la clase Comunidad
        """
        num_ciudadanos = 20000
        infectados = 10
        prom_conexion_fisica = 10
        prob_conexión_fisica = 40
        comunidad = Comunidad(num_ciudadanos, enfermedad, infectados,
                            prom_conexion_fisica, prob_conexión_fisica)
        """
        Se realiza la simulación
        """
        dias_simulacion = 60
        simulacion = Simulacion(dias_simulacion, comunidad, enfermedad)
        simulacion.simular()


class MyApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='cl.com.Example',
                        flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.create_action("about", self.on_about_action)


    def on_about_action(self, action, param):
        about = Gtk.AboutDialog.new()
        about.set_authors(['Cristian Pavez', 'Felipe Mendez', 'Alejandro Ide'])
        about.set_comments("Esta en progreso")
        about.set_program_name("Simulación")
        about.set_copyright("Ing. Civil en Bioinformática")
        about.set_visible(True)


    def do_activate(self):
        active_window = self.props.active_window
        if active_window:
            active_window.present()
        else:
            self.win = MainWindow(application=self)
            self.win.present()


    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f'app.{name}', shortcuts)


if __name__ == '__main__':
    app = MyApp()
    app.run(sys.argv)
