import flet as ft

from ui.libro_from import libro_from

def main_window(page: ft.Page):
    page.title = "Sistema de Biblioteca Universitaria"
    page.window_width = 1100
    page.window_height = 700
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_50

    #Ejemplo de widget: Text
    titulo = ft.Text(
        "Sistema de Biblioteca Universitaria",
        size=24,
        weight=ft.FontWeight.BOLD,
        color = ft.Colors.BLUE_GREY_900
    )

    subtitulo = ft.Text(
        "Seleccione una opción del menú",
        size = 16,
        color = ft.Colors.BLUE_GREY_600
    )

    # Widget Conteiner
    contenido = ft.Container(
        padding = 30,
        expand = True
    )

    def inicio():
        return ft.Column(
            controls = [
                titulo,
                subtitulo
            ], 
            spacing = 10,
        )
    
    def mostrar_inicio(e = None):
        contenido.content = inicio()
        page.update()
    
    def mostrar_insertar_libros(e = None):
        contenido.content = libro_from(mostrar_inicio)
        page.update()

    #Reacciona al click del botón de libros en el menú lateral

    menu_lateral = ft.Container(
        width = 220,
        bgcolor = ft.Colors.BLUE_GREY_900,
        padding = 20,
        content = ft.Column(
            controls = [
                ft.Text(
                    "Biblioteca",
                    size = 22,
                    weight = ft.FontWeight.BOLD,
                    color = ft.Colors.WHITE
                ),
                ft.Text(
                    "Sistema de gestión",
                    size = 12,
                    color = ft.Colors.BLUE_GREY_100
                ),

                ft.Divider(color = ft.Colors.BLUE_GREY_700),
                ft.ElevatedButton(
                    "Inicio", 
                    icon = ft.Icons.HOME,
                    width = 180,
                    on_click = mostrar_inicio
                ),

                ft.ElevatedButton(
                    "Libros",
                    icon = ft.Icons.BOOK,
                    width = 180,
                    on_click = mostrar_insertar_libros
                ),
                ft.ElevatedButton(
                    "Usuarios",
                    icon = ft.Icons.PERSON,
                    width = 180,
                ),
                ft.ElevatedButton(
                    "Prestamos",
                    icon = ft.Icons.SWAP_HORIZ,
                    width = 180,
                ),
                ft.ElevatedButton(
                    "Devoluciones",
                    icon = ft.Icons.KEYBOARD_RETURN,
                    width = 180,
                ),
            ],
            spacing = 15
        )
    )

    layout = ft.Row(
        controls = [
            menu_lateral,
            contenido
        ],
        expand = True
    )

    page.add(layout)