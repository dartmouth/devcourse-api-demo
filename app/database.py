"""SQLite engine + session helper (SQLModel / SQLAlchemy)."""

from sqlmodel import SQLModel, create_engine, Session
from typing import Iterator

# The SQLite file lives in the project root.  Using `sqlite:///` works on Windows & *nix.
SQLITE_URL = "sqlite:///./coffee.db"

engine = create_engine(
    SQLITE_URL,
    echo=False,          # Set to True for SQL logging while debugging
    connect_args={"check_same_thread": False},  # Needed for SQLite + FastAPI
)

def create_db_and_tables() -> None:
    """Create tables if they don't exist yet."""
    SQLModel.metadata.create_all(engine)

def get_session() -> Iterator[Session]:
    """FastAPI dependency that provides a DB session and closes it after the request."""
    with Session(engine) as session:
        yield session