import sys
import gi
import matplotlib

gi.require_version('Gtk', '4.0')
matplotlib.use('TkAgg')

from gi.repository import Gio, Gtk
from time import sleep
from simulacion import Simulacion
from enfermedad import Enfermedad
from comunidad import Comunidad


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        """
        Genera la venta y todas sus partes
        """
        super().__init__(*args, **kwargs)
        self.app = self.get_application()
        self.set_default_size(1920, 1080)
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
        # Crear la ventana
        self.scroll = Gtk.ScrolledWindow()
        self.main_box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)
        self.data_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 5)
        self.set_child(self.scroll)
        self.scroll.set_child(self.main_box)
        self.main_box.append(self.data_box)
        # self.valor = self.make_entry("valor", 10)
        # Entry 1 = Infeccion probable
        self.entry_infeccion_probable = Gtk.Entry()
        self.make_entry(self.entry_infeccion_probable, "Probabilidad de infectar:")
        self.valor_base(self.entry_infeccion_probable, 5)

        # Entry 2 = Infeccion estrecho
        self.entry_infeccion_estrecho = Gtk.Entry()
        self.make_entry(self.entry_infeccion_estrecho, "Probabilidad de infectar a un contacto estrecho:")
        self.valor_base(self.entry_infeccion_estrecho, 20)

        # Entry 3 = promedio de pasos
        self.entry_promedio_pasos = Gtk.Entry()
        self.make_entry(self.entry_promedio_pasos, "Promedio de pasos (días con la infección):")
        self.valor_base(self.entry_promedio_pasos, 10)

        # Entry 4 = Mortalidad
        self.entry_mortalidad = Gtk.Entry()
        self.make_entry(self.entry_mortalidad, "Mortalidad de la infección:")
        self.valor_base(self.entry_mortalidad, 2)

        # Entry 5 = Número de ciudadanos
        self.entry_num_ciudadanos = Gtk.Entry()
        self.make_entry(self.entry_num_ciudadanos, "Cantidad de ciudadanos en la comunidad:")
        self.valor_base(self.entry_num_ciudadanos, 20000)

        # Entry 6 = Número de infectados iniciales
        self.entry_infectados = Gtk.Entry()
        self.make_entry(self.entry_infectados, "Cantidad de infectados iniciales:")
        self.valor_base(self.entry_infectados, 10)

        # Entry 7 = Promedio de coneccion fisica
        self.entry_prom_coneccion_fisica = Gtk.Entry()
        self.make_entry(self.entry_prom_coneccion_fisica, "Promedio de conecciones por persona:")
        self.valor_base(self.entry_prom_coneccion_fisica, 7)

        # Entry 8 = Probabilidad de coneccion fisica
        self.entry_prob_coneccion_fisica = Gtk.Entry()
        self.make_entry(self.entry_prob_coneccion_fisica, "Probabilidad de que la coneecion sea estrecha:")
        self.valor_base(self.entry_prob_coneccion_fisica, 40)

        # Entry 9 = Cantidad de dias de la simulación
        self.entry_dias_simulacion = Gtk.Entry()
        self.make_entry(self.entry_dias_simulacion, "Dias de la simualción:")
        self.valor_base(self.entry_dias_simulacion, 60)

        self.box_espacio = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 10)
        self.box_espacio.set_vexpand(True)
        self.data_box.append(self.box_espacio)

        # Botón para empezar la simualción
        self.start_button = Gtk.Button.new_with_label("Empezar simulación")
        self.start_button.connect("clicked",self.on_start_button_clicked)
        self.data_box.append(self.start_button)

        self.image = Gtk.Image.new()
        self.image.set_pixel_size(1000)
        self.main_box.append(self.image)
        self.image.set_hexpand(True)



    def make_entry(self, entry, texto):
        box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 10)
        self.data_box.append(box)
        label = Gtk.Label.new(texto)
        label.set_margin_start(10)
        label.set_hexpand(True)
        label.set_halign(1)
        box.append(label)
        entry.set_margin_end(10)
        box.append(entry)




    def cajas_vacias(self, box):
        box2 = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 10)
        box.append(box2)
        pass


    def valor_base(self, entry, numero):
        entry.set_text(f"{numero}")


    def on_start_button_clicked(self, button):
        """
        Tiene la funcion de generar una bandera para que se ingresen bien los datos
        """
        # REALIZAR BIEN ESTA BANDERA
        if not self.entry_infeccion_probable.get_text().isnumeric():
            print("Se ingreso un valor no valido para 'infeccion probable'")
        elif not self.entry_infeccion_estrecho.get_text().isnumeric():
            print("Se ingreso un valor no valido para 'infeccion estrecho'")
        elif not self.entry_promedio_pasos.get_text().isnumeric():
            print("Se ingreso un valor no valido para 'promedio de pasos'")
        elif not self.entry_mortalidad.get_text().isnumeric():
            print("Se ingreso un valor no valido para 'mortalidad'")
        elif not self.entry_num_ciudadanos.get_text().isnumeric():
            print("Se ingreso un valor no valido para 'numero de ciudadanos'")
        elif not self.entry_infectados.get_text().isnumeric():
            print("Se ingreso un valor no valido para 'numero de infectados iniciales'")
        elif not self.entry_prom_coneccion_fisica.get_text().isnumeric():
            print("Se ingreso un valor no valido para 'promedio de coneccion fisicas'")
        elif not self.entry_prob_coneccion_fisica.get_text().isnumeric():
            print("Se ingreso un valor no valido para 'probabilidad de coneccion fisica'")
        elif not self.entry_dias_simulacion.get_text().isnumeric():
            print("Se ingreso un valor no valido para 'cantidad de dias de la simulacion'")
        else:
            if int(self.entry_infeccion_probable.get_text()) > 100:
                print("Ese valor es muy alto, elija un numero menor o igual a 100")
            elif int(self.entry_infeccion_probable.get_text()) < 1:
                print("Ese valor es muy bajo, elija un numero mayor o igual a 1")
            elif int(self.entry_infeccion_estrecho.get_text()) > 100:
                print("Ese valor es muy alto, elija un numero menor o igual a 100")
            elif int(self.entry_infeccion_estrecho.get_text()) < 1:
                print("Ese valor es muy bajo, elija un numero mayor o igual a 1")
            elif int(self.entry_mortalidad.get_text()) > 100:
                print("Ese valor es muy alto, elija un numero menor o igual a 100")
            elif int(self.entry_mortalidad.get_text()) < 1:
                print("Ese valor es muy bajo, elija un numero mayor o igual a 1")
            elif int(self.entry_prob_coneccion_fisica.get_text()) > 100:
                print("Ese valor es muy alto, elija un numero menor o igual a 100")
            elif int(self.entry_prob_coneccion_fisica.get_text()) < 1:
                print("Ese valor es muy bajo, elija un numero mayor o igual a 1")
            elif int(self.entry_num_ciudadanos.get_text()) < 1:
                print("Se necesita de almenos 1 persona en la poblacion, elija un numero mayor")
            elif int(self.entry_infectados.get_text()) < 1:
                print("Se necesita de almenos 1 infectados, elija un numero mayor")
            elif int(self.entry_infectados.get_text()) > int(self.entry_num_ciudadanos.get_text()):
                print("No pueden ser mas infetados iniciales que la misma cantidad de poblacion")
            else:
                self.iniciar_simulacion()


    def iniciar_simulacion(self):
        """
        Valores bases para la clase Enfermedad, Comunidad y Simulacion
        """
        # Datos para la clase Enfermedad
        infeccion_probable = int(self.entry_infeccion_probable.get_text())
        infeccion_estrecho = int(self.entry_infeccion_estrecho.get_text())
        promedio_pasos = int(self.entry_promedio_pasos.get_text())
        mortalidad = int(self.entry_mortalidad.get_text())
        enfermedad = Enfermedad(infeccion_probable, infeccion_estrecho,
                                promedio_pasos, mortalidad)
        # Datos para la clase Comunidad
        num_ciudadanos = int(self.entry_num_ciudadanos.get_text())
        infectados = int(self.entry_infectados.get_text())
        prom_coneccion_fisica = int(self.entry_prom_coneccion_fisica.get_text())
        prob_coneccion_fisica = int(self.entry_prob_coneccion_fisica.get_text())
        comunidad = Comunidad(num_ciudadanos, enfermedad, infectados,
                            prom_coneccion_fisica, prob_coneccion_fisica)
        # Datos para la clase Simulacion
        dias_simulacion = int(self.entry_dias_simulacion.get_text())
        simulacion = Simulacion(dias_simulacion, comunidad, enfermedad)
        while simulacion.get_dias() != simulacion.get_contador():
            simulacion.simular()
            self.image.set_from_pixbuf(simulacion.mostrar_grafico())


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
