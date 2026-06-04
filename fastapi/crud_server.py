# Annotated permite declarar tipos con metadatos extra (aquí, la dependencia de FastAPI)
from typing import Annotated

# FastAPI: framework web | Depends: inyección de dependencias | HTTPException: errores HTTP
from fastapi import Depends, FastAPI, HTTPException
# BaseModel: define esquemas de datos (validación y serialización JSON)
from pydantic import BaseModel
# String: tipo de columna texto | create_engine: conexión a la base de datos
from sqlalchemy import String, create_engine
# DeclarativeBase: clase base para modelos ORM
# Mapped: anota el tipo de cada columna
# Session: sesión activa contra la BD
# mapped_column: define una columna en la tabla
# sessionmaker: fábrica que crea sesiones reutilizables
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

# --- CONFIGURACIÓN DE LA BASE DE DATOS ---

# Ruta del archivo SQLite. "sqlite:///" indica el driver; "./users.db" es el archivo local
DATABASE_URL = "sqlite:///./users.db"

# Motor: objeto central que gestiona la conexión con SQLite
# connect_args={"check_same_thread": False} permite que FastAPI use la BD desde distintos hilos
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal es una fábrica: cada llamada SessionLocal() abre una sesión nueva contra el engine
SessionLocal = sessionmaker(bind=engine)


# Clase base de la que heredan todos los modelos (tablas)
class Base(DeclarativeBase):
    pass


# Modelo ORM: representa la tabla "users" en Python
class User(Base):
    __tablename__ = "users"  # Nombre real de la tabla en SQLite

    id: Mapped[int] = mapped_column(primary_key=True)  # Clave primaria autoincremental
    name: Mapped[str] = mapped_column(String(100))  # Texto de hasta 100 caracteres
    email: Mapped[str] = mapped_column(String(100), unique=True)  # Email único por usuario


# Esquema de entrada al crear un usuario (lo que envía el cliente en el POST)
class UserCreate(BaseModel):
    name: str
    email: str


# Esquema de entrada al actualizar: todos los campos son opcionales
class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None


# Esquema de salida: lo que devuelve la API al cliente
class UserOut(BaseModel):
    id: int
    name: str
    email: str

    # Permite construir UserOut desde un objeto SQLAlchemy (User)
    model_config = {"from_attributes": True}


# Crea la tabla "users" en el archivo users.db si aún no existe
Base.metadata.create_all(bind=engine)

# Instancia principal de la aplicación FastAPI
app = FastAPI()


# Dependencia que provee una sesión de BD por petición HTTP
def get_db():
    db = SessionLocal()  # Abre una sesión nueva
    try:
        yield db  # Entrega la sesión al endpoint que la necesite
    finally:
        db.close()  # Siempre cierra la sesión al terminar la petición


# Atajo de tipo: cualquier parámetro "db: Db" recibe automáticamente una Session
Db = Annotated[Session, Depends(get_db)]


# POST /users — crear usuario
@app.post("/users", response_model=UserOut)
def create_user(data: UserCreate, db: Db):
    user = User(name=data.name, email=data.email)  # Objeto Python → fila pendiente
    db.add(user)  # Marca el usuario para insertar
    db.commit()  # Ejecuta el INSERT en SQLite
    db.refresh(user)  # Recarga el objeto con el id generado por la BD
    return user


# GET /users — listar todos los usuarios
@app.get("/users", response_model=list[UserOut])
def list_users(db: Db):
    return db.query(User).all()  # SELECT * FROM users


# GET /users/{id} — obtener un usuario por id
@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Db):
    user = db.get(User, user_id)  # Busca por clave primaria
    if not user:
        raise HTTPException(404, "Usuario no encontrado")
    return user


# PUT /users/{id} — actualizar nombre y/o email
@app.put("/users/{user_id}", response_model=UserOut)
def update_user(user_id: int, data: UserUpdate, db: Db):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(404, "Usuario no encontrado")
    if data.name is not None:
        user.name = data.name  # Modifica el campo en memoria
    if data.email is not None:
        user.email = data.email
    db.commit()  # Persiste los cambios con UPDATE
    db.refresh(user)  # Sincroniza el objeto con la BD
    return user


# DELETE /users/{id} — eliminar usuario
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Db):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(404, "Usuario no encontrado")
    db.delete(user)  # Marca la fila para borrar
    db.commit()  # Ejecuta el DELETE en SQLite
    return {"ok": True}
