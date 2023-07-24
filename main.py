import sys
from time import sleep
import concurrent.futures
import gi
import matplotlib
gi.require_version('Gtk', '4.0')
matplotlib.use('TkAgg')
from gi.repository import Gio, Gtk

from simulacion import Simulacion
from enfermedad import Enfermedad
from comunidad import Comunidad
from vacuna import Vacuna
from mensaje import Mensaje


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
        # Label titulo 1
        self.make_label_title("Valores de la Enfermedad")
        # Entry 1 = Infeccion probable
        self.entry_infeccion_probable = self.make_entry("Probabilidad de infectar:",
                                                        '5')
        # Entry 2 = Infeccion estrecho
        self.entry_infeccion_estrecho = self.make_entry("Probabilidad de infectar a un contacto estrecho:",
                                                        '20')
        # Entry 3 = promedio de pasos
        self.entry_promedio_pasos = self.make_entry("Promedio de pasos (días con la infección):",
                                                    '10')
        # Entry 4 = Mortalidad
        self.entry_mortalidad = self.make_entry("Mortalidad de la infección:",
                                                '2')
        # Label titulo 2
        self.make_label_title("Valores de la Comunidad")
        # Entry 5 = Número de ciudadanos
        self.entry_num_ciudadanos = self.make_entry("Cantidad de ciudadanos en la comunidad:",
                                                    '20000')
        # Entry 6 = Número de infectados iniciales
        self.entry_infectados = self.make_entry("Cantidad de infectados iniciales:",
                                                '10')
        # Entry 7 = Promedio de coneccion fisica
        self.entry_prom_coneccion_fisica = self.make_entry("Promedio de conecciones por persona:",
                                                            '7')
        # Entry 8 = Probabilidad de coneccion fisica
        self.entry_prob_coneccion_fisica = self.make_entry("Probabilidad de que la coneccion sea estrecha:",
                                                            '20')
        # Label titulo 3
        self.make_label_title("Valores de la Simulación")
        # Entry 9 = Cantidad de dias de la simulación
        self.entry_dias_simulacion = self.make_entry("Dias de la simualción:",
                                                    '60')
        # Label titulo 4
        self.make_label_title("Valores de la Vacuna")
        # Entry 10 = Cantidad de vacunas (%)
        self.entry_porc_vacunas = self.make_entry("Porcentaje de población a vacunar:",
                                                    '40')
        # Entry 11 = Inicio vacunación
        self.entry_inicio_vacunacion = self.make_entry("Día de incio de vacunación:",
                                                    '4')
        # Entry 12 = Tasa de vacunación (Personas por día)
        self.entry_tasa_vacunacion = self.make_entry("Tasa de vacunación (porcentaje de la población por día):",
                                                    '1')
        # Entry 13 = porcentaje de inmunidad 1
        self.entry_porc_inmu_1 = self.make_entry("Porcentaje de inmunidad de la vacuna 1 (25%):",
                                                    '100')
        # Entry 14 = porcentaje de inmunidad 2
        self.entry_porc_inmu_2 = self.make_entry("Porcentaje de inmunidad de la vacuna 2 (50%):",
                                                    '50')
        # Entry 15 = porcentaje de inmunidad 3
        self.entry_porc_inmu_3 = self.make_entry("Porcentaje de inmunidad de la vacuna 3 (25%):",
                                                    '20')
        # Label titulo 5
        self.make_label_title("Leyenda")
        # Labels de la leyenda
        self.make_label("Poblacion sana total<span foreground='red'><big> ◉ </big></span>Rojo")
        self.make_label("Poblacion enferma total<span foreground='yellow'><big> ◉ </big></span>Amarillo")
        self.make_label("Poblacion enferma nueva<span foreground='blue'><big> ◉ </big></span>Azul")
        self.make_label("Poblacion muerta total<span foreground='green'><big> ◉ </big></span>Verde")
        self.make_label("Poblacion vacunada total<span foreground='purple'><big> ◉ </big></span>Morado")
        self.make_label("Poblacion inmune por la vacuna<span foreground='brown'><big> ◉ </big></span>Café")
        # box de espacio
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
        self.progreso = None


    def make_label_title(self, texto):
        """
        Esta funcion crea un label con tan solo una frase para uso como titulo
        """
        label = Gtk.Label()
        label.set_markup(f"<span foreground='blue'><big><i><b>{texto}</b></i></big></span>")
        label.set_margin_start(15)
        label.set_halign(1)
        label.set_hexpand(True)
        self.data_box.append(label)


    def make_label(self, texto):
        """
        Esta funcion crea un label con tan solo una frase
        """
        label = Gtk.Label()
        label.set_markup(f"<i><b>{texto}</b></i>")
        label.set_margin_start(30)
        label.set_halign(1)
        label.set_hexpand(True)
        self.data_box.append(label)


    def make_entry(self, texto, inicial):
        """
        Esta funcion crea un bloque de espacio con un texto y un entry para valores
        """
        entry = Gtk.Entry()
        entry.set_text(inicial)
        entry.set_margin_end(10)
        box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 10)
        label = Gtk.Label.new(texto)
        label.set_margin_start(30)
        label.set_halign(1)
        label.set_hexpand(True)
        box.append(label)
        box.append(entry)
        self.data_box.append(box)
        return entry


    def on_start_button_clicked(self, button):
        """
        Tiene la funcion de generar una bandera para que se ingresen bien los datos
        """
        # REALIZAR BIEN ESTA BANDERA
        if not self.entry_infeccion_probable.get_text().isnumeric():
            self.show_mensaje("Error",
                            "Se ingreso un valor no numérico en: 'Probabilidad de infectar'.",
                            True)
        elif not self.entry_infeccion_estrecho.get_text().isnumeric():
            self.show_mensaje("Error",
                              "Se ingreso un valor no numérico en: 'Probabilidad de infectar a un contacto estrecho'.",
                              True)
        elif not self.entry_promedio_pasos.get_text().isnumeric():
            self.show_mensaje("Error",
                              "Se ingreso un valor no numérico en: 'Promedio de pasos'.",
                              True)
        elif not self.entry_mortalidad.get_text().isnumeric():
            self.show_mensaje("Error",
                              "Se ingreso un valor no numérico en: 'Mortalidad de la infección'.",
                              True)
        elif not self.entry_num_ciudadanos.get_text().isnumeric():
            self.show_mensaje("Error",
                              "Se ingreso un valor no numérico en: 'Cantidad de ciudadanos en la comunidad'.",
                              True)
        elif not self.entry_infectados.get_text().isnumeric():
            self.show_mensaje("Error",
                              "Se ingreso un valor no numérico en: 'Cantidad de infectados iniciales'.",
                              True)
        elif not self.entry_prom_coneccion_fisica.get_text().isnumeric():
            self.show_mensaje("Error",
                              "Se ingreso un valor no numérico en: 'promedio de conexiones por persona'.",
                              True)
        elif not self.entry_prob_coneccion_fisica.get_text().isnumeric():
            self.show_mensaje("Error",
                              "Se ingreso un valor no numérico en: 'Probabilidad de que la conexión sea estrecha'.",
                              True)
        elif not self.entry_dias_simulacion.get_text().isnumeric():
            self.show_mensaje("Error",
                              "Se ingreso un valor no numérico en: 'Días de la simulacion'.",
                              True)
        elif not self.entry_porc_vacunas.get_text().isnumeric():
            self.show_mensaje("Error",
                              "Se ingreso un valor no numérico en: 'Porcentaje de la población a vacunar'.",
                              True)
        elif not self.entry_inicio_vacunacion.get_text().isnumeric():
            self.show_mensaje("Error",
                              "Se ingreso un valor no numérico en: 'Día de inicio de la vacunación'.",
                              True)
        elif not self.entry_tasa_vacunacion.get_text().isnumeric():
            self.show_mensaje("Error",
                              "Se ingreso un valor no numérico en: 'Tasa de vacunación'.",
                              True)
        elif not self.entry_porc_inmu_1.get_text().isnumeric():
            self.show_mensaje("Error",
                              "Se ingreso un valor no numérico en: 'Porcentaje de inmunidad de la vacuna 1'.",
                              True)
        elif not self.entry_porc_inmu_2.get_text().isnumeric():
            self.show_mensaje("Error",
                              "Se ingreso un valor no numérico en: 'Porcentaje de inmunidad de la vacuna 2'.",
                              True)
        elif not self.entry_porc_inmu_3.get_text().isnumeric():
            self.show_mensaje("Error",
                              "Se ingreso un valor no numérico en: 'Porcentaje de inmunidad de la vacuna 3'.",
                              True)
        else:
            if int(self.entry_infeccion_probable.get_text()) > 100:
                self.show_mensaje("Error",
                                  "'Probabilidad de infectar' no puede ser mayor que 100.",
                                  True)
            elif int(self.entry_infeccion_probable.get_text()) < 0:
                self.show_mensaje("Error",
                                  "'Probabilidad de infectar' no puede ser menor que 0.",
                                  True)
            elif int(self.entry_infeccion_estrecho.get_text()) > 100:
                self.show_mensaje("Error",
                                  "'Probabilidad de infectar a un contacto estrecho' no puede ser mayor que 100.",
                                  True)
            elif int(self.entry_infeccion_estrecho.get_text()) < 0:
                self.show_mensaje("Error",
                                  "'Probabilidad de infectar a un contacto estrecho' no puede ser menor que 0",
                                  True)
            elif int(self.entry_promedio_pasos.get_text()) > 100:
                self.show_mensaje("Error",
                                  "'Promedio de pasos' no puede ser mayor que 100.",
                                  True)
            elif int(self.entry_promedio_pasos.get_text()) < 0:
                self.show_mensaje("Error",
                                  "'Promedio de pasos' no puede ser menor que 0.",
                                  True)
            elif int(self.entry_mortalidad.get_text()) > 100:
                self.show_mensaje("Error",
                                  "'Mortalidad de la infección' no puede ser mayor que 100",
                                  True)
            elif int(self.entry_mortalidad.get_text()) < 0:
                self.show_mensaje("Error",
                                  "'Mortalidad de la infección' no puede ser menor que 0.",
                                  True)
            elif int(self.entry_prom_coneccion_fisica.get_text()) > 100:
                self.show_mensaje("Error",
                                  "'Promedio de conexiones por persona' no puede ser mayor que 100.",
                                  True)
            elif int(self.entry_prom_coneccion_fisica.get_text()) < 0:
                self.show_mensaje("Error",
                                  "'Promedio de conexiones por persona' no puede ser menor que 0.",
                                  True)
            elif int(self.entry_prob_coneccion_fisica.get_text()) > 100:
                self.show_mensaje("Error",
                                  "'Probabilidad de que la conexión sea estrecha' no puede ser mayor que 100.",
                                  True)
            elif int(self.entry_prob_coneccion_fisica.get_text()) < 0:
                self.show_mensaje("Error",
                                  "'Probabilidad de que la conexión sea estrecha' no puede ser menor que 0.",
                                  True)
            elif int(self.entry_num_ciudadanos.get_text()) < 1:
                self.show_mensaje("Error",
                                  "'Cantidad de ciudadanos en la comunidad' no puede ser menor que 1.",
                                  True)
            elif int(self.entry_infectados.get_text()) < 1:
                self.show_mensaje("Error",
                                  "'Cantidad de infectados iniciales' no puede ser menor que 1.",
                                  True)
            elif int(self.entry_infectados.get_text()) > int(self.entry_num_ciudadanos.get_text()):
                self.show_mensaje("Error",
                                  "'Cantidad de infectados iniciales' no puede ser mayor que 'Cantidad de ciudadanos en la comunidad'.",
                                  True)
            elif int(self.entry_dias_simulacion.get_text()) < 1:
                self.show_mensaje("Error",
                                  "'Días de la simulación' no puede ser menor que 1.",
                                  True)
            elif int(self.entry_porc_vacunas.get_text()) < 0:
                self.show_mensaje("Error",
                                  "'Porcentaje de población a vacunar' no puede ser menor que 0.",
                                  True)
            elif int(self.entry_porc_vacunas.get_text()) > 100:
                self.show_mensaje("Error",
                                  "'Porcentaje de población a vacunar' no puede ser mayor que 100.",
                                  True)
            elif int(self.entry_inicio_vacunacion.get_text()) < 1:
                self.show_mensaje("Error",
                                  "'Día de inicio de vacunación' no puede ser menor que 1.",
                                  True)
            elif int(self.entry_inicio_vacunacion.get_text()) > int(self.entry_dias_simulacion.get_text()):
                self.show_mensaje("Error",
                                  "'Día de inicio de vacunación' no puede ser mayor que 'Días de la simulación'.",
                                  True)
            elif float(self.entry_tasa_vacunacion.get_text()) < 0:
                self.show_mensaje("Error",
                                  "'Tasa de vacunación' no puede ser menor que 0.",
                                  True)
            elif float(self.entry_tasa_vacunacion.get_text()) > 100:
                self.show_mensaje("Error",
                                  "'Tasa de vacunación' no puede ser mayor que 100.",
                                  True)
            elif int(self.entry_porc_inmu_1.get_text()) < 0:
                self.show_mensaje("Error",
                                  "'Porcentaje de inmunidad de la vacuna 1' no puede ser menor que 0.",
                                  True)
            elif int(self.entry_porc_inmu_1.get_text()) > 100:
                self.show_mensaje("Error",
                                  "'Porcenje de inmunidad de la vacuna 1' no puede ser mayor que 100.",
                                  True)
            elif int(self.entry_porc_inmu_2.get_text()) < 0:
                self.show_mensaje("Error",
                                  "'Porcenje de inmunidad de la vacuna 2' no puede ser menor que 0.",
                                  True)
            elif int(self.entry_porc_inmu_2.get_text()) > 100:
                self.show_mensaje("Error",
                                  "Porcenaje de inmunidad de la vacuna 2' no puede ser mayor que 100.",
                                  True)
            elif int(self.entry_porc_inmu_3.get_text()) < 0:
                self.show_mensaje("Error",
                                  "'Porcentaje de inmunidad de la vacuna 3' no puede ser menor que 0.",
                                  True)
            elif int(self.entry_porc_inmu_3.get_text()) > 100:
                self.show_mensaje("Error",
                                  "'Porcentaje de inmunidad de la vacuna 3' no puede ser mayor que 100.",
                                  True)
            else:
                self.show_mensaje("Realizando simulación",
                                  "Espere un momento por favor...", False)
                self.iniciar_simulacion()
                self.progreso.close()

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
        # Datos para la clase Vacunas
        inicio_vacunacion = int(self.entry_inicio_vacunacion.get_text())
        total_vacunas = num_ciudadanos*int(self.entry_porc_vacunas.get_text())/100
        tasa = float(self.entry_tasa_vacunacion.get_text())
        inmunidades = [int(self.entry_porc_inmu_1.get_text()), int(self.entry_porc_inmu_2.get_text()), int(self.entry_porc_inmu_3.get_text())]
        distribucion_vacunas = [total_vacunas * 25 / 100, total_vacunas * 50 / 100,
                                total_vacunas * 25 / 100]
        vacunas = []
        for i in range(3):
            vacuna = Vacuna(distribucion_vacunas[i], inmunidades[i])
            vacunas.append(vacuna)

        # Datos para la clase Simulacion
        dias_simulacion = int(self.entry_dias_simulacion.get_text())
        simulacion = Simulacion(dias_simulacion, comunidad, enfermedad,
                                inicio_vacunacion, total_vacunas, tasa, vacunas)
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(simulacion.simular())
        self.image.set_from_pixbuf(simulacion.mostrar_grafico())


    def show_mensaje(self, title, texto, button):
        mensaje = Mensaje(parent=self.get_root(), title=title, texto=texto,
                          button=button)
        if button:
            mensaje.connect("response", self.on_mensaje_response)
        else:
            self.progreso = mensaje
        mensaje.set_visible(True)


    def on_mensaje_response(self, dialog, response):
        """Confirma que el usuario haya presionado el bótón para cerrar la ventana"""
        if response == Gtk.ResponseType.OK:
            dialog.close()


class MyApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='cl.com.Example',
                        flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.create_action("about", self.on_about_action)


    def on_about_action(self, action, param):
        about = Gtk.AboutDialog.new()
        about.set_authors(['Cristian Pavez', 'Felipe Mendez', 'Alejandro Ide'])
        about.set_comments("Este programa simula una ola de infecciones de un virus en una población")
        about.set_program_name("Simulación de un Virus")
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
