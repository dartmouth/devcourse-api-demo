"""FastAPI Router – wires HTTP verbs & paths to controller functions."""

from typing import Optional

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.database import get_session
from app.controllers.coffee import (
    create_coffee,
    delete_coffee,
    get_coffee,
    list_coffees,
    recommend_coffee,
)
from app.schemas.coffee import CoffeeCreate, CoffeeRead, CoffeeRecommendation

router = APIRouter()


@router.post(
    "/",
    response_model=CoffeeRead,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new coffee drink",
)
def create(payload: CoffeeCreate, session: Session = Depends(get_session)):
    return create_coffee(payload, session)


@router.get("/", response_model=list[CoffeeRead], summary="List all coffee drinks")
def read_all(session: Session = Depends(get_session)):
    return list_coffees(session)


@router.get(
    "/recommendation",
    response_model=CoffeeRecommendation,
    summary="Get a coffee recommendation for the time of day",
)
def recommendation(time_of_day: Optional[str] = None):
    """Pure business logic – no database session involved.

    Not every endpoint needs to touch the database: this one computes an
    answer from its input (or the server clock) and a set of rules living
    entirely in the service layer. Try `?time_of_day=evening`.
    """
    return recommend_coffee(time_of_day)


# NOTE: this route MUST be declared before `/{coffee_id}` below, otherwise
# FastAPI would treat "recommendation" as a coffee_id and 422 on the int
# conversion.
@router.get("/{coffee_id}", response_model=CoffeeRead, summary="Get a coffee drink by its ID")
def read_one(coffee_id: int, session: Session = Depends(get_session)):
    return get_coffee(coffee_id, session)


@router.delete("/{coffee_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a coffee drink")
def delete(coffee_id: int, session: Session = Depends(get_session)):
    delete_coffee(coffee_id, session)
    return None


# ------------------------------------------------------------------
# PATCH – comment/uncomment together with the service & controller
# ------------------------------------------------------------------
# @router.patch(
#     "/{coffee_id}",
#     response_model=CoffeeCreate,
#     summary="Partially update a coffee drink",
# )
# def patch(coffee_id: int, payload: CoffeeUpdate):
#     return update_coffee(coffee_id, payload)