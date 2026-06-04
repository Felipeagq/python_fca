from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

# --- CONFIGURACIÓN DE LA BASE DE DATOS ---

DATABASE_URL = "sqlite:///./users.db"  # Archivo local users.db
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100),nullable=True)


# --- OPERACIONES CRUD ---

def create_user(name: str, email: str) -> User:
    db = SessionLocal()
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user


def list_users() -> list[User]:
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users


def get_user(user_id: int) -> User | None:
    db = SessionLocal()
    user = db.get(User, user_id)
    db.close()
    return user


def update_user(user_id: int, name: str | None = None, email: str | None = None) -> User | None:
    db = SessionLocal()
    user = db.get(User, user_id)
    if not user:
        db.close()
        return None
    for field, value in {"name": name, "email": email}.items():
        if value is not None:
            setattr(user, field, value)
    db.commit()
    db.refresh(user)
    db.close()
    return user


def delete_user(user_id: int) -> bool:
    db = SessionLocal()
    user = db.get(User, user_id)
    if not user:
        db.close()
        return False
    db.delete(user)
    db.commit()
    db.close()
    return True



