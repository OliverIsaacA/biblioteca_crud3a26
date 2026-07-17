import flet as ft

from dao.libro_dao import LibroDAO

def libros_list(regresar):
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Título")),
            ft.DataColumn(ft.Text("Autor")),
            ft.DataColumn(ft.Text("ISBN")),
            ft.DataColumn(ft.Text("Disponible")),
        ],
        rows = []
    )

    mensaje = ft.Text("")

    def cargar_libros():
        try:
            libro_dao = LibroDAO()
            libros = libro_dao.obtener_todos()

            tabla.rows.clear()

            #Colocamos la información de un libro dentro de la tabla
            for libro in libros:
                tabla.rows.append(
                    ft.DataRow(
                        cells = [
                            ft.DataCell(ft.Text(str(libro.id))),
                            ft.DataCell(ft.Text(libro.titulo)),
                            ft.DataCell(ft.Text(libro.autor)),
                            ft.DataCell(ft.Text(libro.isbn)),
                            ft.DataCell(ft.Text(libro.disponible))
                        ]
                    )
                )
        except Exception as error:
            mensaje.value = f"Error al consultar libros: {error}"
            mensaje.color = ft.Colors.RED