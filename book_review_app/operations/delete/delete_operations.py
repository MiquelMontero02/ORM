from sqlalchemy.orm import Session
from models import Usuario, Autor, Libro, Reseña

def borrar_instancia(session: Session, instancia) -> bool:
    """
    Borra una instancia específica de la base de datos.

    Args:
        session (Session): La sesión de la base de datos SQLAlchemy.
        instancia (DeclarativeMeta): Objeto instancia del modelo a borrar.

    Returns:
        bool: True si la instancia fue borrada, False si la instancia es None.
    """
    if instancia is None:
        return False
    session.delete(instancia)
    session.commit()
    return True


def borrar_usuario(session: Session, usuario: Usuario) -> bool:
    """
    Borra un usuario dado.

    Args:
        session (Session): La sesión de la base de datos.
        usuario (Usuario): Instancia de Usuario a borrar.

    Returns:
        bool: True si el usuario fue borrado, False si no existe.
    """
    return borrar_instancia(session, usuario)


def borrar_autor(session: Session, autor: Autor) -> bool:
    """
    Borra un autor dado.

    Args:
        session (Session): La sesión de la base de datos.
        autor (Autor): Instancia de Autor a borrar.

    Returns:
        bool: True si el autor fue borrado, False si no existe.
    """
    return borrar_instancia(session, autor)


def borrar_libro(session: Session, libro: Libro) -> bool:
    """
    Borra un libro dado.

    Args:
        session (Session): La sesión de la base de datos.
        libro (Libro): Instancia de Libro a borrar.

    Returns:
        bool: True si el libro fue borrado, False si no existe.
    """
    return borrar_instancia(session, libro)


def borrar_reseña(session: Session, reseña: Reseña) -> bool:
    """
    Borra una reseña dada.

    Args:
        session (Session): La sesión de la base de datos.
        reseña (Reseña): Instancia de Reseña a borrar.

    Returns:
        bool: True si la reseña fue borrada, False si no existe.
    """
    return borrar_instancia(session, reseña)
