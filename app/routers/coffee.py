"""FastAPI Router – wires HTTP verbs & paths to controller functions."""

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.database import get_session
from app.controllers.coffee import (
    create_coffee,
    delete_coffee,
    get_coffee,
    list_coffees,
)
from app.schemas.coffee import CoffeeCreate, CoffeeRead

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