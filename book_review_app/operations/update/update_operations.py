from sqlalchemy.orm import Session
from models import Usuario, Autor, Libro, Reseña

def actualizar_campo(session: Session, instancia, field: str, nuevo_valor) -> object:
    """
    Actualiza un campo específico de una instancia del modelo sin modificar otros datos sensibles como claves foráneas.

    Args:
        session (Session): Sesión activa de SQLAlchemy.
        instancia (DeclarativeMeta): Instancia de modelo.
        field (str): Campo a modificar.
        nuevo_valor: Nuevo valor que se quiere asignar al campo.

    Returns:
        object: Instancia actualizada.

    Raises:
        AttributeError: Si el campo no existe en la instancia.
    """
    if instancia is None:
        return None

    if not hasattr(instancia, field):
        raise AttributeError(f"La instancia '{type(instancia).__name__}' no tiene un campo '{field}'.")

    setattr(instancia, field, nuevo_valor)

    try:
        session.commit()
        session.refresh(instancia)
        return instancia
    except Exception as e:
        session.rollback()
        raise e



def actualizar_usuario_email(session: Session, usuario: Usuario, nuevo_email: str) -> Usuario:
    """
    Actualiza el email de un usuario dado.

    Args:
        session (Session): La sesión de la base de datos.
        usuario (Usuario): Instancia de Usuario a actualizar.
        nuevo_email (str): Nuevo email a asignar.

    Returns:
        Usuario: Usuario actualizado o None si no existe.
    """
    return actualizar_campo(session, usuario, "email", nuevo_email)


def actualizar_autor_nombre(session: Session, autor: Autor, nuevo_nombre: str) -> Autor:
    """
    Actualiza el nombre de un autor dado.

    Args:
        session (Session): La sesión de la base de datos.
        autor (Autor): Instancia de Autor a actualizar.
        nuevo_nombre (str): Nuevo nombre a asignar.

    Returns:
        Autor: Autor actualizado o None si no existe.
    """
    return actualizar_campo(session, autor, "nombre", nuevo_nombre)


def actualizar_libro_titulo(session: Session, libro: Libro, nuevo_titulo: str) -> Libro:
    """
    Actualiza el título de un libro dado.

    Args:
        session (Session): La sesión de la base de datos.
        libro (Libro): Instancia de Libro a actualizar.
        nuevo_titulo (str): Nuevo título a asignar.

    Returns:
        Libro: Libro actualizado o None si no existe.
    """
    return actualizar_campo(session, libro, "titulo", nuevo_titulo)


def actualizar_reseña_puntuacion(session: Session, reseña: Reseña, nueva_puntuacion: float) -> Reseña:
    """
    Actualiza la puntuación de una reseña dada.

    Args:
        session (Session): La sesión de la base de datos.
        reseña (Reseña): Instancia de Reseña a actualizar.
        nueva_puntuacion (float): Nueva puntuación a asignar.

    Returns:
        Reseña: Reseña actualizada o None si no existe.
    """
    return actualizar_campo(session, reseña, "puntuacion", nueva_puntuacion)
