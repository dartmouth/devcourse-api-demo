"""SQLModel definition that maps directly to a SQLite table."""

from typing import Optional
from sqlmodel import Field, SQLModel


class Coffee(SQLModel, table=True):
    """
    Persistence layer – represents a row in the `coffee` table.
    Only the fields that belong in the DB are defined here.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, description="Name of the drink, e.g. 'Latte'")
    price: float = Field(description="Price in USD")
    # You can later add more fields (origin, roast, etc.) without touching the rest
    # of the code – just a new column in the DB and an entry in the schema.