from sqlalchemy.orm import Session
from sqlalchemy.exc import ArgumentError
from models import Usuario, Autor, Libro, Reseña

def obtener_usuario_por_id(session: Session, usuario_id: int) -> Usuario:
    return obtener_por_campo(session, Usuario, "id", usuario_id)

def obtener_autor_por_id(session: Session, autor_id: int) -> Autor:
    return obtener_por_campo(session, Autor, "id", autor_id)

def obtener_libro_por_id(session: Session, libro_id: int) -> Libro:
    return obtener_por_campo(session, Libro, "id", libro_id)

def obtener_reseña_por_id(session: Session, reseña_id: int) -> Reseña:
    return obtener_por_campo(session, Reseña, "id", reseña_id)

def obtener_por_campo(session: Session, modelo, field: str, value) -> object:
    """
    Busca un registro en la base de datos por un campo y valor específicos.

    Args:
        session (Session): La sesión de la base de datos SQLAlchemy.
        modelo (DeclarativeMeta): La clase del modelo (por ejemplo, Usuario, Autor, etc.).
        field (str): El nombre del campo/atributo del modelo para filtrar.
        value: El valor que debe coincidir en el campo.

    Returns:
        object: La primera instancia encontrada que cumple el filtro, o None si no hay coincidencias.

    Raises:
        AttributeError: Si el campo especificado no existe en el modelo.
    """
    if not hasattr(modelo, field):
        raise AttributeError(f"El modelo '{modelo.__name__}' no tiene un campo '{field}'")

    filtro = getattr(modelo, field) == value
    return session.query(modelo).filter(filtro).first()

# Ejemplos específicos reutilizando la función genérica

