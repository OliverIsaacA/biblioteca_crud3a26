
from dao.libro_dao import LibroDAO
from models.libro import Libro

def ver_libros():
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

def insertar_libro():
    titulo = input("Escribe el título del nuevo libro: ")
    autor = int(input("Escribe el id del autor: "))
    isbn = input("Escribe el isbn del nuevo libro: ")
    disponible = True
    try:
        libro_dao = LibroDAO()
        id = libro_dao.obtener_ultimo_id() + 1
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.insertar(libro)
        print("Inserción realizada con éxito")
    except Exception as e:
        print("Error al insertar un nuevo libro")
        print(e)

def eliminar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libros disponibles: ")
        ver_libros()
        id = int(input("Escribe el id del libro a eliminar: "))
        libro_dao.eliminar(id)
        print(f"El libro {id} ha sido eliminado con éxito")
    except Exception as e:
        print(f"Error al eliminar el libro {id}")
        print(e)

def menu_libros():
    print("1. Ver todos los libros")
    print("2. Insertar un libro nuevo")
    print("3. Actualizar un libro disponible")
    print("4. Eliminar un libro disponible")
    opcion = int(input("Seleccionar una opcion (1-4): "))

    match opcion:
        case 1:
            ver_libros()
        case 2:
            insertar_libro()
        case 3:
            actualizar_libro()
        case 4:
            eliminar_libro()


def menu_usuarios():
    print("1. Ver todos los usuarios")
    print("2. Insertar un usuario nuevo")
    print("3. Actualizar un usuario disponible")
    print("4. Eliminar un usuario disponible")
    opcion = int(input("Seleccionar una opcion (1-4): "))

    match opcion:
        case 1:
            ver_usuarios()
        case 2:
            insertar_usuario()
        case 3:
            actualizar_usuario()
        case 4:
            eliminar_usuario()


def actualizar_libro():
    print("Selecciona el libro a actualizar")
    try:
        libro_dao = LibroDAO()
        ver_libros()
        id = int(input("Escribe el id del libro a actualizar: "))
        titulo = input("Escribe el nuevo título")
        autor = input("Escribe el nuevo autor")
        isbn = input("Escribe el nuevo ISBN")
        disponible = bool(input("Escribe el nuevo valor de disponible"))
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.actualizar(libro)
        print(f"El libro {id} se ha actualizado exitosamente")

    except Exception as e:
        print("Error al actualizar un libro")
        print(e)


#============================================================#
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

def ver_usuarios():
    try:
        usuario_dao = UsuarioDAO()

        usuarios = usuario_dao.obtener_todo()

        print("=== Lista de usuarios ===")

        if len(usuarios) == 0:
            print("No hay usuarios registrados.")
        else:
            for usuario in usuarios: 
                print("====================================")
                print(
                    f"ID: {usuario.id}, Nombre: {usuario.nombre}, "
                    f"Matrícula: {usuario.matricula}, Carrera: {usuario.carrera}, "
                    f"Correo: {usuario.correo}"
                    
                )
                print("====================================")
        print("\n Conexión exitosa a la base de datos")
    except Exception as e:
        print("Error: ")
        print(e)

def insertar_usuario():
    nombre = input("Escribe el nombre del nuevo usuario: ")
    matricula = input("Escribe la matrícula del nuevo usuario: ")
    carrera = input("Escribe la carrera del nuevo usuario: ")
    correo = input("Escribe el correo del nuevo usuario: ")
    try:
        usuario_dao = UsuarioDAO()
        id = usuario_dao.obtener_ultimo_id() + 1
        usuario = Usuario(id, nombre, matricula, carrera, correo)
        usuario_dao.insertar(usuario)
        print("Inserción realizada con éxito")
    except Exception as e:
        print("Error al insertar un nuevo usuario")
        print(e)

def eliminar_usuario():
    try:
        usuario_dao = UsuarioDAO()
        print("Lista de usuarios disponibles: ")
        ver_usuarios()
        id = int(input("Escribe el id del usuario a eliminar: "))
        usuario_dao.eliminar(id)
        print(f"El usuario {id} ha sido eliminado con éxito")
    except Exception as e:
        print(f"Error al eliminar el usuario {id}")
        print(e)


def actualizar_usuario():
    print("Selecciona al usuario a actualizar")
    try:
        usuario_dao = UsuarioDAO()
        ver_usuarios()
        id = int(input("Escribe el id del usuario a actualizar: "))
        nombre = input("Escribe el nuevo nombre")
        matricula = input("Escribe la nueva matrícula")
        carrera = input("Escribe la nueva carrera")
        correo = input("Escribe el nuevo correo")
        usuario = Usuario(id, nombre, matricula, carrera, correo)
        usuario_dao.actualizar(usuario)
        print(f"El usuario {id} se ha actualizado exitosamente")

    except Exception as e:
        print("Error al actualizar un usuario")
        print(e)

def main():
    print("=== BIBLIOTECA UNIVERSITARIA ===")
    print("Menú de opciones")
    print  ("1. Libros")
    print("2. Usuarios")
    
    opc = int(input("Selecciona una opcion: "))

    match opc:
        case 1:
            menu_libros()
        case 2:
            menu_usuarios()    
 


if __name__ == "__main__":
    main()
