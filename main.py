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
        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=Gio.Menu())
        menu_button.set_create_popup_func(self.clicked_menu_button)
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
        # Valores para la clase Enfermedad
        infeccion_probable = 5
        # int, porcentaje de infeccion para contactos estrechos
        infeccion_estrecho = 70
        # int, numero medio de pasos (días) para ser declarado sano o muerto
        promedio_pasos = 10
        # int, porcentaje de mortalidad para el enfermo
        mortalidad = 2                                               
        #Se le entregan los valores a la clase
        enfermedad = Enfermedad(infeccion_probable, infeccion_estrecho,
                                promedio_pasos, mortalidad)
        """
        Valores bases para la clase Comunidad
        """
        # int, cantidad de población incial
        num_ciudadanos = 2000
        # int, cantidad de infectados inciales
        infectados = 10
        # int, indica la media de conecciones físicas que tiene una persona
        prom_conexion_fisica = 10
        # int, indica la probabiliadad que el contacto físico sea un contacto estrecho
        prob_conexión_fisica = 100
        #Se le entregan los valores a la clase
        comunidad = Comunidad(num_ciudadanos, enfermedad, infectados,
                            prom_conexion_fisica, prob_conexión_fisica)
        """
        Se realiza la simulación
        """
        # int, dias que dura la simulacion
        dias_simulacion = 60
        #Se le entregan los valores a la clase, como los objetos ya hechos
        simulacion = Simulacion(dias_simulacion, comunidad, enfermedad)
        #Se hace la simulacion
        simulacion.simular()

    
    def clicked_menu_button(self, button):
        # Crear el about Dialog
        about_header = Gtk.AboutDialog.new()
        about_header.set_authors(['Cristian Pavez', 'Felipe Mendez', 'Alejandro Ide'])
        about_header.set_program_name(self.get_title()) 
        about_header.show()


class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def do_activate(self):
        active_window = self.props.active_window
        if active_window:
            active_window.present()
        else:
            self.win = MainWindow(application=self)
            self.win.present()
        

app = MyApp(application_id="com.uwu",flags= Gio.ApplicationFlags.FLAGS_NONE)
app.run(sys.argv)
