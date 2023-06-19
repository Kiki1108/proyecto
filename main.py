import sys
import gi
import matplotlib

gi.require_version('Gtk', '4.0')

from gi.repository import Gio, Gtk
from time import sleep
from simulacion import Simulacion
from enfermedad import Enfermedad
from comunidad import Comunidad
matplotlib.use('TkAgg')


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        """
        Genera la venta y todas sus partes
        """
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
        # Crear la ventana
        self.main_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 5)
        self.set_child(self.main_box)
        # Entry 1 = Infeccion probable
        self.box_1 = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 20)
        self.main_box.append(self.box_1)
        self.label_1 = Gtk.Label()
        self.label_1.set_label("Infeccion probable:")
        self.label_1.set_hexpand(True)
        self.label_1.set_halign(1)
        self.label_1.set_margin_start(10)
        self.box_1.append(self.label_1)
        self.entry_infeccion_probable = Gtk.Entry()
        self.entry_infeccion_probable.set_text("5")
        self.entry_infeccion_probable.set_margin_end(10)        
        self.box_1.append(self.entry_infeccion_probable)
        # Entry 2 = Infeccion estrecho
        self.box_2 = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 20)
        self.main_box.append(self.box_2)
        self.label_2 = Gtk.Label()
        self.label_2.set_label("Infeccion estrecho:")
        self.label_2.set_margin_start(10)
        self.label_2.set_hexpand(True)
        self.label_2.set_halign(1)
        self.box_2.append(self.label_2)
        self.entry_infeccion_estrecho = Gtk.Entry()
        self.entry_infeccion_estrecho.set_text("70")
        self.entry_infeccion_estrecho.set_margin_end(10)
        self.box_2.append(self.entry_infeccion_estrecho)
        # Entry 3 = promedio de pasos
        self.box_3 = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 20)
        self.main_box.append(self.box_3)
        self.label_3 = Gtk.Label()
        self.label_3.set_label("Promedio de pasos:")
        self.label_3.set_margin_start(10)
        self.label_3.set_hexpand(True)
        self.label_3.set_halign(1)
        self.box_3.append(self.label_3)
        self.entry_promedio_pasos = Gtk.Entry()
        self.entry_promedio_pasos.set_text("10")
        self.entry_promedio_pasos.set_margin_end(10)
        self.box_3.append(self.entry_promedio_pasos)
        # Entry 4 = Mortalidad
        self.box_4 = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 20)
        self.main_box.append(self.box_4)
        self.label_4 = Gtk.Label()
        self.label_4.set_label("Mortalidad:")
        self.label_4.set_margin_start(10)
        self.label_4.set_hexpand(True)
        self.label_4.set_halign(1)
        self.box_4.append(self.label_4)
        self.entry_mortalidad = Gtk.Entry()
        self.entry_mortalidad.set_text("2")
        self.entry_mortalidad.set_margin_end(10)        
        self.box_4.append(self.entry_mortalidad)
        # Entry 5 = Número de ciudadanos
        self.box_5 = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 20)
        self.main_box.append(self.box_5)
        self.label_5 = Gtk.Label()
        self.label_5.set_label("Número de ciudadanos:")
        self.label_5.set_margin_start(10)
        self.label_5.set_hexpand(True)
        self.label_5.set_halign(1)
        self.box_5.append(self.label_5)
        self.entry_num_ciudadanos = Gtk.Entry()
        self.entry_num_ciudadanos.set_text("20000")
        self.entry_num_ciudadanos.set_margin_end(10)
        self.box_5.append(self.entry_num_ciudadanos)
        # Entry 6 = Número de infectados iniciales
        self.box_6 = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 20)
        self.main_box.append(self.box_6)
        self.label_6 = Gtk.Label()
        self.label_6.set_label("Número de infectados iniciales:")
        self.label_6.set_margin_start(10)
        self.label_6.set_hexpand(True)
        self.label_6.set_halign(1)
        self.box_6.append(self.label_6)
        self.entry_infectados = Gtk.Entry()
        self.entry_infectados.set_text("10")
        self.entry_infectados.set_margin_end(10)
        self.box_6.append(self.entry_infectados)
        # Entry 7 = Promedio de coneccion fisica
        self.box_7 = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 20)
        self.main_box.append(self.box_7)
        self.label_7 = Gtk.Label()
        self.label_7.set_label("Promedio de coneccion fisica:")
        self.label_7.set_margin_start(10)
        self.label_7.set_hexpand(True)
        self.label_7.set_halign(1)
        self.box_7.append(self.label_7)
        self.entry_prom_coneccion_fisica = Gtk.Entry()
        self.entry_prom_coneccion_fisica.set_text("10")
        self.entry_prom_coneccion_fisica.set_margin_end(10)
        self.box_7.append(self.entry_prom_coneccion_fisica)
        # Entry 8 = Probabilidad de coneccion fisica
        self.box_8 = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 20)
        self.main_box.append(self.box_8)
        self.label_8 = Gtk.Label()
        self.label_8.set_label("Probabilidad de coneccion fisica:")
        self.label_8.set_margin_start(10)
        self.label_8.set_hexpand(True)
        self.label_8.set_halign(1)
        self.box_8.append(self.label_8)
        self.entry_prob_coneccion_fisica = Gtk.Entry()
        self.entry_prob_coneccion_fisica.set_text("40")
        self.entry_prob_coneccion_fisica.set_margin_end(10)
        self.box_8.append(self.entry_prob_coneccion_fisica)
        # Entry 9 = Cantidad de dias de la simulación
        self.box_9 = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 20)
        self.main_box.append(self.box_9)
        self.label_9 = Gtk.Label()
        self.label_9.set_label("Cantidad de dias de la simulación:")
        self.label_9.set_margin_start(10)
        self.label_9.set_hexpand(True)
        self.label_9.set_halign(1)
        self.box_9.append(self.label_9)
        self.entry_dias_simulacion = Gtk.Entry()
        self.entry_dias_simulacion.set_text("60")
        self.entry_dias_simulacion.set_margin_end(10)
        self.box_9.append(self.entry_dias_simulacion)
        # Botón para empezar la simualción
        self.start_button = Gtk.Button.new_with_label("Empezar simulación")
        self.start_button.connect("clicked",self.on_start_button_clicked)
        self.main_box.append(self.start_button)


    def on_start_button_clicked(self, button):
        """
        Tiene la funcion de generar una bandera para que se ingresen bien los datos
        """
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
        prob_conexión_fisica = int(self.entry_prob_coneccion_fisica.get_text())
        comunidad = Comunidad(num_ciudadanos, enfermedad, infectados,
                            prom_coneccion_fisica, prob_conexión_fisica)
        # Datos para la clase Simulacion
        dias_simulacion = int(self.entry_dias_simulacion.get_text())
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
