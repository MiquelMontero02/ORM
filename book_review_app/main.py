from database import engine
from models import Base

def crear_base_de_datos():
    """
    Crea todas las tablas definidas en los modelos dentro de la base de datos.

    Utiliza la metadata de SQLAlchemy para crear las tablas si no existen.
    """
    Base.metadata.create_all(bind=engine)
    print("Base de datos y tablas creadas.")

if __name__ == "__main__":
    crear_base_de_datos()
