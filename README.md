# ORM Project with SQLAlchemy and Flask

Primer proyecto trabajando con [SQLAlchemy](https://www.sqlalchemy.org/) y Flask para entender cómo funciona un ORM.

*First project working with [SQLAlchemy](https://www.sqlalchemy.org/) and Flask to understand how ORM works.*

## ¿Qué veremos en este proyecto?

Este proyecto busca explicar los fundamentos del ORM de Python [SQLAlchemy](https://www.sqlalchemy.org/).  
Contempla la creación de una base de datos mediante el uso del ORM, junto con dos secciones para realizar operaciones CRUD y aplicar funciones de agregación.

Además, utiliza __[Alembic](https://alembic.sqlalchemy.org/en/latest/)__, una herramienta de migraciones para bases de datos en Python diseñada para usarse con SQLAlchemy.  
Alembic facilita gestionar y versionar cambios en el esquema de la base de datos (crear, modificar o eliminar tablas y columnas) de forma controlada y automatizada, apoyando la evolución del esquema durante el desarrollo.

*This project aims to explain the fundamentals of the Python ORM [SQLAlchemy](https://www.sqlalchemy.org/).*  
*It includes creating a database with the ORM and two sections for CRUD operations and aggregation functions.*

*Additionally, it uses __[Alembic](https://alembic.sqlalchemy.org/en/latest/)__, a migration tool for Python databases designed to work with SQLAlchemy.*  
*Alembic helps manage and version changes in the database schema (create, modify, or drop tables and columns) in a controlled and automated way, supporting schema evolution during development.*

## ¿Qué es un ORM?

Un _Object-Relational Mapping_ (__ORM__) permite trabajar con bases de datos relacionales usando conceptos y estructuras de la Programación Orientada a Objetos (__POO__).  

Su objetivo es crear un vínculo entre las tablas y relaciones de bases de datos SQL y las clases y objetos definidos en POO.

*An _Object-Relational Mapping_ (__ORM__) allows working with relational databases using concepts and structures from Object-Oriented Programming (__OOP__).*  

*Its goal is to create a link between tables and relationships in SQL databases and the classes and objects defined in OOP.*

## Ventajas

- **Abstracción:** Evita mezclar sentencias SQL puras con el código de la aplicación.  
- **Seguridad:** Añade una capa para evitar ataques de SQL Injection.  
- **Portabilidad:** Permite cambiar de base de datos fácilmente.

*Advantages*  

- **Abstraction:** Avoids mixing raw SQL statements with application code.  
- **Security:** Adds a layer to prevent SQL Injection attacks.  
- **Portability:** Allows easy switching between databases.

## ¿Se puede usar un ORM sin conocimientos de SQL?

Aunque el ORM facilita la interacción con bases de datos, es importante conocer su funcionamiento para optimizar su uso.  
Conceptos como las relaciones entre clases, optimización de consultas y funciones de agregación son esenciales para sacarle el máximo provecho.

También es indispensable dominar las operaciones CRUD _(Create, Read, Update, Delete)_, básicas en cualquier base de datos relacional.

*Can you use an ORM without SQL knowledge?*

*While the ORM makes database interaction easier, understanding how it works is important for optimization.*  
*Concepts such as class relationships, query optimization, and aggregation functions are essential to fully benefit from an ORM.*

*It is also crucial to master CRUD operations _(Create, Read, Update, Delete)_, fundamental in any relational database.*

---

## Tecnologías usadas

- [Python](https://www.python.org/)  
- [Flask](https://flask.palletsprojects.com/)  
- [SQLAlchemy](https://www.sqlalchemy.org/)  
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)  

---