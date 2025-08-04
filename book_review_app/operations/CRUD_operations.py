from database import SessionLocal
from models import Usuario, Autor, Libro, Reseña
from sqlalchemy import select

db = SessionLocal()

# 🔍 Leer todos los libros
print("\n--- Libros disponibles ---")
for libro in db.scalars(select(Libro)).all():
    print(f"{libro.id}: {libro.titulo} ({libro.año_publicacion}) - Autor: {libro.autor.nombre}")

# 🔍 Consultar reseñas de un libro
print("\n--- Reseñas de 'Cien Años de Soledad' ---")
libro = db.scalars(select(Libro).where(Libro.titulo == "Cien Años de Soledad")).first()
for r in libro.reseñas:
    print(f"{r.usuario.nombre} ({r.puntuacion}/5): {r.contenido}")

# ✍️ Agregar un nuevo usuario
nuevo_usuario = Usuario(nombre="María López", email="maria@example.com")
db.add(nuevo_usuario)
db.commit()

# 🔄 Actualizar puntuación de una reseña
reseña = db.scalars(select(Reseña).where(Reseña.puntuacion < 4)).first()
if reseña:
    reseña.puntuacion = 4
    db.commit()
    print(f"Actualizada reseña #{reseña.id}")

# ❌ Eliminar un usuario
usuario = db.scalars(select(Usuario).where(Usuario.nombre == "Luis Pérez")).first()
if usuario:
    db.delete(usuario)
    db.commit()
    print("Usuario eliminado.")

db.close()
