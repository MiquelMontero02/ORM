from sqlalchemy.orm import Session
from models import Usuario, Autor, Libro, Reseña

def crear_usuario(session: Session, usuario: Usuario) -> Usuario:
    """
    Agrega un objeto Usuario a la base de datos.

    Args:
        session (Session): La sesión de la base de datos SQLAlchemy.
        usuario (Usuario): Instancia del modelo Usuario con los datos a insertar.

    Returns:
        Usuario: La instancia de Usuario persistida con ID asignado.
    """
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

def crear_autor(session: Session, autor: Autor) -> Autor:
    """
    Agrega un objeto Autor a la base de datos.

    Args:
        session (Session): La sesión de la base de datos SQLAlchemy.
        autor (Autor): Instancia del modelo Autor con los datos a insertar.

    Returns:
        Autor: La instancia de Autor persistida con ID asignado.
    """
    session.add(autor)
    session.commit()
    session.refresh(autor)
    return autor

def crear_libro(session: Session, libro: Libro) -> Libro:
    """
    Agrega un objeto Libro a la base de datos.

    Args:
        session (Session): La sesión de la base de datos SQLAlchemy.
        libro (Libro): Instancia del modelo Libro con los datos a insertar.

    Returns:
        Libro: La instancia de Libro persistida con ID asignado.
    """
    session.add(libro)
    session.commit()
    session.refresh(libro)
    return libro

def crear_reseña(session: Session, reseña: Reseña) -> Reseña:
    """
    Agrega un objeto Reseña a la base de datos.

    Args:
        session (Session): La sesión de la base de datos SQLAlchemy.
        reseña (Reseña): Instancia del modelo Reseña con los datos a insertar.

    Returns:
        Reseña: La instancia de Reseña persistida con ID asignado.
    """
    session.add(reseña)
    session.commit()
    session.refresh(reseña)
    return reseña
