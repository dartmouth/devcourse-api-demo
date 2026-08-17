"""Thin layer that turns FastAPI request/response objects into service calls.

Each function returns a Pydantic schema (or raises an HTTPException) – the
router then handles turning that into JSON + proper status code.
"""

from typing import Optional

from fastapi import HTTPException
from sqlmodel import Session

from app.schemas.coffee import CoffeeCreate, CoffeeRead, CoffeeRecommendation
from app.services.coffee import CoffeeService


def create_coffee(payload: CoffeeCreate, session: Session) -> CoffeeRead:
    coffee = CoffeeService.create(session, payload)
    return CoffeeRead.model_validate(coffee)


def list_coffees(session: Session) -> list[CoffeeRead]:
    coffees = CoffeeService.list_all(session)
    return [CoffeeRead.model_validate(c) for c in coffees]


def get_coffee(coffee_id: int, session: Session) -> CoffeeRead:
    coffee = CoffeeService.get_by_id(session, coffee_id)
    if coffee is None:
        raise HTTPException(status_code=404, detail="Coffee not found")
    return CoffeeRead.model_validate(coffee)


def delete_coffee(coffee_id: int, session: Session) -> dict:
    success = CoffeeService.delete(session, coffee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Coffee not found")
    return {"detail": "Deleted successfully"}


def recommend_coffee(time_of_day: Optional[str] = None) -> CoffeeRecommendation:
    """No `session` parameter here – this doesn't touch the database at all."""
    period, drink, reason = CoffeeService.recommend(time_of_day)
    return CoffeeRecommendation(time_of_day=period, recommendation=drink, reason=reason)

# ----------------------------------------------------------------------
# PATCH controller (commented out – enable when you have time)
# ----------------------------------------------------------------------
# def update_coffee(
#     coffee_id: int,
#     payload: CoffeeUpdate,
#     session: Session = Depends(get_session),
# ) -> CoffeeRead:
#     coffee = CoffeeService.update(session, coffee_id, payload)
#     if coffee is None:
#         raise HTTPException(status_code=404, detail="Coffee not found")
#     return CoffeeRead.model_validate(coffee)