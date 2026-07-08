import flet as ft

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
        weight=ft.Fontweight.BOLD
    )

    subtitulo = ft.Text(
        "Seleccione una opción del menú",
        size = 16,
        color = ft.Colors.BLUE_GREY_600
    )

    # Widget Conteiner
    contenido = ft.Conteiner(
        content = ft.Column(
            controls = [
                titulo,
                subtitulo
            ], 
            spacing = 10,
        ),
        padding = 30,
        expanded = True
    )

    menu_lateral = ft.Container(
        width = 220,
        bgcolor = ft.Colors.BLUE_GREY_900,
        padding = 20,
        content = ft.Column(
            controls = [
                ft.Text(
                    "Biblioteca",
                    size = 22,
                    weight = ft.Fontweight.BOLD,
                    color = ft.Colors.WHITE
                ),
                ft.Text(
                    "Sistema de gestión",
                    size = 12,
                    color = ft.Colors.BLUE_GREY_100
                ),
                ft.Divider(color = ft.Colors.BLUE_GREY_700),
                ft.ElevatedButton(
                    text = "Libros",
                    text = ft.Icons.BOOK,
                    width = 100,
                ),
                ft.ElevatedButton(
                    text = "Usuarios",
                    text = ft.Icons.PERSON,
                    width = 100,
                ),
                ft.ElevatedButton(
                    text = "Prestamos",
                    text = ft.Icons.SWAP_HORIZ,
                    width = 100,
                ),
                ft.ElevatedButton(
                    text = "Devoluciones",
                    text = ft.Icons.KEYBOARD_RETURN,
                    width = 100,
                ),
            ],
            spacing = 15
        )
    )

    layout = ft.Row(
        controls = (
            menu_lateral,
            contenido
        ),
        expand = True
    )

    page.add(layout)