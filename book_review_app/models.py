from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, timezone
from database import Base

class Usuario(Base):
    """
    Representa un usuario del sistema.

    :ivar id: Identificador único del usuario (clave primaria).
    :vartype id: int
    :ivar nombre: Nombre completo del usuario.
    :vartype nombre: str
    :ivar email: Correo electrónico único del usuario.
    :vartype email: str
    :ivar fecha_creacion: Fecha y hora en que se creó el usuario (UTC).
    :vartype fecha_creacion: datetime
    :ivar reseñas: Lista de reseñas realizadas por el usuario.
    :vartype reseñas: List[Reseña]
    """
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    fecha_creacion: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))

    reseñas = relationship("Reseña", back_populates="usuario")


class Autor(Base):
    """
    Representa un autor de libros.

    :ivar id: Identificador único del autor (clave primaria).
    :vartype id: int
    :ivar nombre: Nombre completo del autor.
    :vartype nombre: str
    :ivar libros: Lista de libros escritos por el autor.
    :vartype libros: List[Libro]
    """
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))

    libros = relationship("Libro", back_populates="autor")


class Libro(Base):
    """
    Representa un libro publicado.

    :ivar id: Identificador único del libro (clave primaria).
    :vartype id: int
    :ivar titulo: Título del libro.
    :vartype titulo: str
    :ivar año_publicacion: Año en que se publicó el libro.
    :vartype año_publicacion: int
    :ivar autor_id: Identificador del autor asociado (clave foránea).
    :vartype autor_id: int
    :ivar autor: Autor del libro.
    :vartype autor: Autor
    :ivar reseñas: Lista de reseñas realizadas sobre el libro.
    :vartype reseñas: List[Reseña]
    """
    __tablename__ = "libros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(200))
    año_publicacion: Mapped[int]
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))

    autor = relationship("Autor", back_populates="libros")
    reseñas = relationship("Reseña", back_populates="libro")


class Reseña(Base):
    """
    Representa una reseña hecha por un usuario a un libro.

    :ivar id: Identificador único de la reseña (clave primaria).
    :vartype id: int
    :ivar contenido: Texto completo de la reseña.
    :vartype contenido: str
    :ivar puntuacion: Puntuación otorgada al libro.
    :vartype puntuacion: float
    :ivar fecha: Fecha en que se realizó la reseña.
    :vartype fecha: datetime
    :ivar usuario_id: Identificador del usuario que hizo la reseña (clave foránea).
    :vartype usuario_id: int
    :ivar libro_id: Identificador del libro reseñado (clave foránea).
    :vartype libro_id: int
    :ivar usuario: Usuario que hizo la reseña.
    :vartype usuario: Usuario
    :ivar libro: Libro reseñado.
    :vartype libro: Libro
    """
    __tablename__ = "reseñas"

    id: Mapped[int] = mapped_column(primary_key=True)
    contenido: Mapped[str] = mapped_column(Text)
    puntuacion: Mapped[float]
    fecha: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    libro_id: Mapped[int] = mapped_column(ForeignKey("libros.id"))

    usuario = relationship("Usuario", back_populates="reseñas")
    libro = relationship("Libro", back_populates="reseñas")
