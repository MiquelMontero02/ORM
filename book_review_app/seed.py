from database import SessionLocal
from book_review_app.models import Usuario, Autor, Libro, Reseña

db = SessionLocal()

# Limpiar datos anteriores
db.query(Reseña).delete()
db.query(Libro).delete()
db.query(Autor).delete()
db.query(Usuario).delete()
db.commit()

# Crear usuarios
usuario1 = Usuario(nombre="Ana Gómez", email="ana@example.com")
usuario2 = Usuario(nombre="Luis Pérez", email="luis@example.com")

# Crear autores
autor1 = Autor(nombre="Gabriel García Márquez")
autor2 = Autor(nombre="Isabel Allende")

# Crear libros
libro1 = Libro(titulo="Cien Años de Soledad", año_publicacion=1967, autor=autor1)
libro2 = Libro(titulo="La Casa de los Espíritus", año_publicacion=1982, autor=autor2)

# Crear reseñas
resena1 = Reseña(contenido="Una obra maestra.", puntuacion=5, usuario=usuario1, libro=libro1)
resena2 = Reseña(contenido="Muy buena narración.", puntuacion=4.5, usuario=usuario2, libro=libro1)
resena3 = Reseña(contenido="Interesante pero algo densa.", puntuacion=3.5, usuario=usuario1, libro=libro2)

# Agregar al session
db.add_all([usuario1, usuario2, autor1, autor2, libro1, libro2, resena1, resena2, resena3])
db.commit()

print("Datos de prueba insertados.")
db.close()
