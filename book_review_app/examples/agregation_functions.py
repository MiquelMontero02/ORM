"""
Script de ejemplo que muestra consultas agregadas sobre libros, reseñas y autores.

Operaciones realizadas:
1. Calcular la puntuación promedio por libro.
2. Contar el número de reseñas por libro.
3. Contar el número de libros por autor.
4. Listar libros destacados con puntuación promedio mayor a 4.0.
"""
import logging

# Silencia los logs de SQLAlchemy
logging.getLogger("sqlalchemy.engine").setLevel(logging.CRITICAL)


from sqlalchemy import select, func
from database import SessionLocal
from models import Libro, Reseña, Autor

def puntuacion_promedio_por_libro(session):
    """
    Muestra la puntuación promedio de cada libro.
    """
    print("\n--- Puntuación promedio por libro ---")
    stmt = (
        select(Libro.titulo, func.avg(Reseña.puntuacion).label("promedio"))
        .join(Reseña, Libro.id == Reseña.libro_id)
        .group_by(Libro.id)
    )
    for titulo, promedio in session.execute(stmt):
        print(f"{titulo}: {promedio:.2f}/5")


def numero_reseñas_por_libro(session):
    """
    Muestra el número total de reseñas para cada libro.
    """
    print("\n--- Número de reseñas por libro ---")
    stmt = (
        select(Libro.titulo, func.count(Reseña.id).label("total_reseñas"))
        .join(Reseña)
        .group_by(Libro.id)
    )
    for titulo, total in session.execute(stmt):
        print(f"{titulo}: {total} reseñas")


def numero_libros_por_autor(session):
    """
    Muestra el número de libros publicados por cada autor.
    """
    print("\n--- Libros por autor ---")
    stmt = (
        select(Autor.nombre, func.count(Libro.id).label("total_libros"))
        .join(Libro, Libro.autor_id == Autor.id)
        .group_by(Autor.id)
    )
    for autor, total in session.execute(stmt):
        print(f"{autor}: {total} libros")


def libros_destacados(session):
    """
    Muestra los libros con una puntuación promedio mayor a 4.0.
    """
    print("\n--- Libros destacados (promedio > 4.0) ---")
    stmt = (
        select(Libro.titulo, func.avg(Reseña.puntuacion).label("promedio"))
        .join(Reseña)
        .group_by(Libro.id)
        .having(func.avg(Reseña.puntuacion) > 4.0)
    )
    for titulo, promedio in session.execute(stmt):
        print(f"{titulo}: {promedio:.2f}/5")


def main():
    session = SessionLocal()
    try:
        puntuacion_promedio_por_libro(session)
        numero_reseñas_por_libro(session)
        numero_libros_por_autor(session)
        libros_destacados(session)
    finally:
        session.close()


if __name__ == "__main__":
    main()
