# examples/ejemplo_operaciones.py

from sqlalchemy import select
from database import SessionLocal
from models import Usuario, Autor, Libro, Reseña

# Importar funciones CRUD (ajusta rutas según tu estructura)
from operations.create.create_operations import crear_usuario
from operations.read.read_operations import *
from operations.update.update_operations import actualizar_reseña_puntuacion
from operations.delete.delete_operations import borrar_usuario


def listar_libros(db):
    """Lista todos los libros con su autor."""
    print("\n--- Libros disponibles ---")
    libros = db.scalars(select(Libro)).all()
    for libro in libros:
        print(f"{libro.id}: {libro.titulo} ({libro.año_publicacion}) - Autor: {libro.autor.nombre}")


def mostrar_reseñas_de_libro(db, titulo: str):
    """Muestra reseñas de un libro por título."""
    print(f"\n--- Reseñas de '{titulo}' ---")
    libro = obtener_por_campo(db,Libro,"titulo" ,titulo)
    if libro:
        for r in libro.reseñas:
            print(f"{r.usuario.nombre} ({r.puntuacion}/5): {r.contenido}")
    else:
        print("Libro no encontrado.")


def agregar_usuario(db):
    """Agrega un nuevo usuario."""
    nuevo_usuario = crear_usuario(db, usuario=Usuario(nombre="María López", email="maria5@example.com"))
    print(f"Usuario creado: {nuevo_usuario.nombre} ({nuevo_usuario.email})")


def actualizar_puntuacion_reseña(db):
    """Actualiza la puntuación de la primera reseña con puntuación menor a 4."""
    reseña = db.query(Reseña).filter(Reseña.puntuacion < 4).first()
    if reseña:
        print(f"\n\n{reseña}\n\n")
        reseña_actualizada = actualizar_reseña_puntuacion(db, reseña, 4.0)
        print(f"Actualizada reseña #{reseña_actualizada.id} con nueva puntuación: {reseña_actualizada.puntuacion}")
    else:
        print("No hay reseñas con puntuación menor a 4.")


def eliminar_usuario(db):
    """Elimina un usuario por nombre."""
    usuario = obtener_por_campo(db,Usuario,"nombre", "Luis Pérez")
    if usuario:
        if borrar_usuario(db, usuario):
            print("Usuario eliminado.")
        else:
            print("Error eliminando usuario.")
    else:
        print("Usuario no encontrado.")


def main():
    db = SessionLocal()
    try:
        listar_libros(db)
        mostrar_reseñas_de_libro(db, "Cien Años de Soledad")
        agregar_usuario(db)
        actualizar_puntuacion_reseña(db)
        eliminar_usuario(db)
    finally:
        db.close()


if __name__ == "__main__":
    main()
