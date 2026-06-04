# python-class

Proyecto de clase para practicar **bases de datos con SQLAlchemy**, **migraciones con Alembic** y (opcionalmente) una **API REST con FastAPI**.

La idea central: en lugar de crear tablas “a mano” con `create_all()`, versionamos cada cambio de la base de datos en archivos de migración que podemos aplicar, revisar y revertir.

---

## ¿Qué hay en este repositorio?

| Archivo / carpeta | Para qué sirve |
|-------------------|----------------|
| `main.py` | Modelo `User`, conexión a SQLite y funciones CRUD en Python puro (sin servidor web). |
| `crud_server.py` | Misma lógica expuesta como API HTTP con FastAPI (endpoints `/users`, etc.). |
| `users.db` | Base de datos SQLite (se genera al aplicar migraciones o al ejecutar la app). |
| `pyproject.toml` | Lista de dependencias del proyecto (FastAPI, SQLAlchemy, Alembic…). |
| `alembic/` | Configuración y **historial de migraciones** de la base de datos. |
| `alembic.ini` | Ajustes generales de Alembic (por ejemplo, la URL de la BD). |

### Flujo mental (de arriba a abajo)

```
Defines el modelo en Python (main.py)
        ↓
Alembic genera un script de migración (alembic/versions/*.py)
        ↓
Aplicas la migración → SQLite (users.db) queda actualizado
        ↓
Tu código (main.py o crud_server.py) lee y escribe datos
```

---

## Requisitos

- **Python 3.13 o superior**
- **[uv](https://docs.astral.sh/uv/)** — gestor de proyectos y dependencias (recomendado en esta clase)

Si aún no tienes `uv`, en macOS/Linux suele bastar:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

En Windows puedes usar el instalador indicado en la [documentación oficial](https://docs.astral.sh/uv/getting-started/installation/).

---

## ¿Qué es `uv` y por qué lo usamos?

**uv** es una herramienta moderna de Astral (los mismos de Ruff) que combina en una sola CLI lo que antes hacías con varias cosas:

| Antes (clásico) | Con uv |
|-----------------|--------|
| Instalar Python con pyenv / instalador del SO | `uv python install 3.13` |
| Crear entorno virtual: `python -m venv .venv` | Se crea automáticamente al sincronizar |
| Activar el venv: `source .venv/bin/activate` | **No hace falta** para ejecutar comandos |
| Instalar paquetes: `pip install -r requirements.txt` | `uv sync` lee `pyproject.toml` |
| Ejecutar un script en ese entorno | `uv run python main.py` |
| Añadir una dependencia | `uv add nombre-paquete` |

### Archivos que debes conocer

- **`pyproject.toml`** — Es el “manifiesto” del proyecto: nombre, versión de Python mínima y lista de dependencias (`fastapi`, `sqlalchemy`, `alembic`, etc.).
- **`.venv/`** — Carpeta del entorno virtual (dependencias instaladas localmente). Suele estar en `.gitignore`; cada alumno la genera en su máquina con `uv sync`.
- **`uv.lock`** (si existe) — Bloquea versiones exactas de los paquetes para que todos el grupo instale lo mismo.

### Comandos que usarás a diario

```bash
# 1. Clonar el repo y entrar en la carpeta
cd python_class

# 2. Crear el entorno e instalar todo lo del pyproject.toml
uv sync

# 3. Ejecutar un archivo Python usando ESE entorno (sin activar nada)
uv run python main.py

# 4. Ejecutar la API (si trabajas con FastAPI)
uv run uvicorn crud_server:app --reload

# 5. Añadir una librería nueva al proyecto (la guarda en pyproject.toml)
uv add httpx

# 6. Cualquier comando de Alembic, también dentro del entorno del proyecto
uv run alembic upgrade head
```

**¿Por qué `uv run`?**  
Le dice a uv: “usa el Python y los paquetes de *este* proyecto”. Así evitas el error típico de ejecutar `python` o `alembic` del sistema y que no encuentre SQLAlchemy o FastAPI.

**Equivalente con pip (solo si no puedes usar uv):**

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
alembic upgrade head
```

En clase preferimos **uv** por velocidad, reproducibilidad y porque no dependes de recordar activar el entorno virtual.

---

## Primer arranque (checklist)

1. Instalar uv (ver arriba).
2. En la raíz del proyecto:

   ```bash
   uv sync
   uv run alembic upgrade head
   ```

3. Probar el CRUD por consola:

   ```bash
   uv run python main.py
   ```

   (Ajusta `main.py` si el profesor dejó un bloque `if __name__ == "__main__"` con ejemplos.)

4. Opcional — levantar la API y abrir la documentación interactiva:

   ```bash
   uv run uvicorn crud_server:app --reload
   ```

   Navegador: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

> **Nota:** `crud_server.py` todavía usa `Base.metadata.create_all()`. En un flujo “solo Alembic”, las tablas las crea `alembic upgrade head` y esa línea no debería usarse. `main.py` ya está pensado para trabajar solo con migraciones.

---

## SQLAlchemy en una frase

- **`engine`** — Conexión con el archivo `users.db`.
- **`SessionLocal`** — Abre una “sesión” para hacer consultas e inserts.
- **`User` (modelo)** — Clase Python que representa la tabla `users` (columnas `id`, `name`, `email`, …).

La URL de la base de datos está en `main.py`:

```python
DATABASE_URL = "sqlite:///./users.db"
```

`sqlite:///./users.db` significa: driver SQLite, archivo `users.db` en la carpeta actual del proyecto.

---

## Alembic: migraciones paso a paso

**Alembic** guarda cada cambio de esquema (nueva tabla, nueva columna, índice…) en un archivo Python dentro de `alembic/versions/`. Así el equipo comparte el mismo historial y la base no “se inventa sola” en cada máquina.

### Paso 1 — Dependencia

En este repo Alembic ya está en `pyproject.toml`. Si partieras de cero:

```bash
uv add alembic
```

### Paso 2 — Inicializar (solo la primera vez en un proyecto nuevo)

```bash
uv run alembic init alembic
```

Genera:

```
alembic/
  env.py          # enlaza Alembic con tus modelos
  versions/       # aquí viven las migraciones
alembic.ini       # configuración
```

*(En este repositorio esto ya está hecho.)*

### Paso 3 — Misma URL en todos sitios

En `alembic.ini`:

```ini
sqlalchemy.url = sqlite:///./users.db
```

Debe coincidir con `DATABASE_URL` en `main.py`. Si cambias una, cambia la otra.

### Paso 4 — Conectar modelos en `alembic/env.py`

Alembic necesita saber qué tablas existen en tu código. En este proyecto ya está configurado así:

```python
from main import DATABASE_URL, Base, User  # User registra la tabla en Base.metadata

config.set_main_option("sqlalchemy.url", DATABASE_URL)
target_metadata = Base.metadata
```

**Importante:** si añades otro modelo (`Post`, `Comment`, …), debes **importarlo** en `env.py` (aunque no lo uses en ese archivo). Si no, `--autogenerate` no lo verá.

### Paso 5 — No uses `create_all` si migras con Alembic

En `main.py` **no** debe quedar:

```python
Base.metadata.create_all(bind=engine)  # ❌ con Alembic, las tablas las crean las migraciones
```

Las tablas aparecen al ejecutar `uv run alembic upgrade head`.

### Paso 6 — Primera migración (proyecto nuevo)

```bash
uv run alembic revision --autogenerate -m "create users table"
```

Alembic compara tus modelos en `main.py` con lo que hay en `users.db` y propone un script en `alembic/versions/`. **Siempre revísalo** antes de aplicarlo: a veces autogenera cosas de más o de menos.

Ejemplo de lo que verás dentro del archivo:

```python
def upgrade() -> None:
    op.create_table("users", ...)

def downgrade() -> None:
    op.drop_table("users")
```

### Paso 7 — Aplicar migraciones

```bash
uv run alembic upgrade head
```

`head` = “la última migración del historial”. Crea o actualiza `users.db`.

---

## Flujo cuando cambias el modelo

Supón que en `main.py` añades una columna `phone` a `User`:

1. Editas el modelo en `main.py`.
2. Generas migración:

   ```bash
   uv run alembic revision --autogenerate -m "add phone to users"
   ```

3. Abres y revisas el archivo nuevo en `alembic/versions/`.
4. Aplicas:

   ```bash
   uv run alembic upgrade head
   ```

5. Vuelves a probar tu script o la API.

Si algo sale mal en la última migración (solo en desarrollo):

```bash
uv run alembic downgrade -1
```

Vuelve un paso atrás en el historial.

---

## Comandos útiles de Alembic

| Comando | Qué hace |
|---------|----------|
| `uv run alembic current` | Qué migración está aplicada ahora |
| `uv run alembic history` | Lista todas las migraciones |
| `uv run alembic upgrade head` | Aplica todas las pendientes |
| `uv run alembic downgrade -1` | Deshace la última migración |
| `uv run alembic stamp head` | Marca la BD como actualizada **sin** ejecutar SQL |

### Caso especial: ya tenías `users.db` con `create_all`

Si la base ya existía antes de configurar Alembic y las tablas coinciden con los modelos:

```bash
uv run alembic stamp head
```

Le dice a Alembic: “considera que ya estoy en la última versión” y evita intentar crear tablas duplicadas.

---

## Resumen visual

```
main.py (modelos SQLAlchemy)
       │
       ▼
uv run alembic revision --autogenerate -m "mensaje"
       │
       ▼
alembic/versions/xxxx_mensaje.py   ← revisar siempre
       │
       ▼
uv run alembic upgrade head
       │
       ▼
users.db actualizada  →  uv run python main.py  /  API FastAPI
```

---

## Problemas frecuentes

| Síntoma | Posible causa | Qué probar |
|---------|---------------|------------|
| `ModuleNotFoundError: sqlalchemy` | Ejecutaste `python` fuera del entorno del proyecto | `uv run python ...` o `uv sync` |
| Alembic no detecta una tabla nueva | Modelo no importado en `env.py` | Añadir `from main import ..., NuevoModelo` |
| `table users already exists` | BD creada a mano y migración intenta crearla otra vez | `uv run alembic stamp head` o borrar `users.db` en desarrollo y `upgrade head` |
| Cambios en el modelo no aparecen en la migración | Olvidaste `--autogenerate` o la BD ya coincide | Revisa `main.py` y el estado con `uv run alembic current` |

---

## Enlaces

- [Documentación de uv](https://docs.astral.sh/uv/)
- [SQLAlchemy 2.0](https://docs.sqlalchemy.org/)
- [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [FastAPI](https://fastapi.tiangolo.com/)
