"""Pydantic schemas that define the public contract of the API.

We keep them separate from the DB model so we never expose internal columns
(e.g., timestamps, internal IDs) unless we explicitly want to.
"""

from typing import Optional
from pydantic import BaseModel, Field, PositiveFloat


class CoffeeBase(BaseModel):
    name: str
    price: PositiveFloat


class CoffeeCreate(CoffeeBase):
    """Payload for POST /coffee/ – all fields required."""
    pass


class CoffeeRead(CoffeeBase):
    """Response model – includes the generated DB id."""
    id: int

    class Config:
        from_attributes = True


class CoffeeRecommendation(BaseModel):
    """Response for GET /coffee/recommendation – no DB row behind this."""
    time_of_day: str
    recommendation: str
    reason: str


class CoffeeUpdate(BaseModel):
    """
    Payload for PATCH /coffee/{id} – all fields optional.
    We keep it separate because PATCH semantics differ from POST.
    """
    name: Optional[str] = Field(None, example="Flat White")
    price: Optional[PositiveFloat] = Field(None, example=4.0)

    class Config:
        from_attributes = True