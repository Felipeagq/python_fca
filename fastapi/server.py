from fastapi import FastAPI, Depends
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker
from sqlalchemy import String, create_engine
from typing import Annotated
from pydantic import BaseModel

DATABASE_URL = "sqlite:///./api_db.db"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100),nullable=True)
    
Base.metadata.create_all(bind=engine)

# Dependencia que provee una sesión de BD por petición HTTP
def get_db():
    db = SessionLocal()  # Abre una sesión nueva
    try:
        yield db  # Entrega la sesión al endpoint que la necesite
    finally:
        db.close()  # Siempre cierra la sesión al terminar la petición


# Atajo de tipo: cualquier parámetro "db: Db" recibe automáticamente una Session
SessionDb = Annotated[Session, Depends(get_db)]

api = FastAPI(
    title="API en clase",
    version="0.1.0",
    description="Esta es una API en clase",
)

# se le pide al usuario en el servidor
class UserSchema(BaseModel):
    id: int | None = None
    name: str
    email: str
    password: str
    
class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: str
    
@api.get("/")
def read_root():
    return {"message": "Hello World"}

@api.get("/{nombre}")
def read_nombre(nombre: str):
    return {"message": f"Hello {nombre}"}

@api.post("/",response_model=UserResponseSchema)
def create_user(
    user: UserSchema, # lo que se le pide al usuario
    db: SessionDb # sesion de db 
    ):
    print(user.model_dump())
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print(db_user)
    return db_user # retornamos los valores


@api.put("/")
def update_user():
    return {"message": "Usuario actualizado"}

@api.delete("/{user_id}")
def delete_user(user_id: int, db: SessionDb):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return {"message": "Usuario no encontrado"}  # o HTTPException 404
    db.delete(db_user)
    db.commit()
    return {"message": "Usuario eliminado"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "server:api", 
        host="localhost", 
        port=8000,
        reload=True,
    )