from dao.libro_dao import LibroDAO
from models.libro import Libro

def main():
    try:
        libro_dao = LibroDAO()

        libros = libro_dao.obtener_todos()

        print("=== Libros en la biblioteca ===")

        if len(libros) == 0:
            print("No hay libros registrados.")
        else:
            for libro in libros: 
                print("====================================")
                print(
                    f"ID: {libro.id}, Título: {libro.titulo}, "
                    f"Autor: {libro.autor}, ISBN: {libro.isbn}, "
                    f"Disponible: {'Si' if libro.disponible else 'No'}"
                )
                print("====================================")
        print("\n Conexión exitosa a la base de datos")
    except Exception as e:
        print("Error: ")
        print(e)

if __name__ == "__main__":
    main()